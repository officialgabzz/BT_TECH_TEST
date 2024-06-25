import datetime
import re
import sys
from typing import Dict, List, Tuple


def output_results(user_data: Dict[str, Dict[str, int]]) -> None:
    """Prints the session data for each user."""
    for username, stats in user_data.items():
        print(f"{username} {stats['sessions']} {stats['total_seconds']}")


def finalize_sessions(
    active_sessions: Dict[str, List[str]],
    end_time: str,
    user_data: Dict[str, Dict[str, int]],
    time_format: str,
) -> Dict[str, Dict[str, int]]:
    """Finalizes any remaining active sessions."""
    for username, start_times in active_sessions.items():
        for start_time in start_times:
            elapsed_seconds = calculate_elapsed_seconds(
                start_time, end_time, time_format
            )
            user_data = update_user_data(username, elapsed_seconds, user_data)
    return user_data


def update_user_data(
    username: str, elapsed_seconds: int, user_data: Dict[str, Dict[str, int]]
) -> Dict[str, Dict[str, int]]:
    """Updates the user data with session count and total elapsed seconds."""
    user_data[username]["sessions"] += 1
    user_data[username]["total_seconds"] += elapsed_seconds
    return user_data


def calculate_elapsed_seconds(start_time: str, end_time: str, time_format: str) -> int:
    """Calculates the elapsed seconds between two times."""
    start = datetime.datetime.strptime(start_time, time_format)
    end = datetime.datetime.strptime(end_time, time_format)
    difference = end - start
    return int(difference.total_seconds())


def initialize_user_data(
    username: str,
    active_sessions: Dict[str, List[str]],
    user_data: Dict[str, Dict[str, int]],
) -> Tuple[Dict[str, Dict[str, int]], Dict[str, List[str]]]:
    """Initializes user data if the user is new."""
    if username not in active_sessions:
        user_data[username] = {"sessions": 0, "total_seconds": 0}
        active_sessions[username] = []
    return user_data, active_sessions


def process_log_entry(
    entry: str,
    user_data: Dict[str, Dict[str, int]],
    time_format: str,
    active_sessions: Dict[str, List[str]],
    first_log_time: str,
) -> Tuple[Dict[str, Dict[str, int]], Dict[str, List[str]]]:
    """Processes each log entry to determine if it is a start or end session."""
    timestamp = entry[:8]
    if "End" in entry:
        username = re.split(r"\s", entry)[1]
        user_data, active_sessions = initialize_user_data(
            username, active_sessions, user_data
        )
        try:
            start_time = active_sessions[username].pop()
        except IndexError:
            start_time = first_log_time
        elapsed_seconds = calculate_elapsed_seconds(start_time, timestamp, time_format)
        user_data = update_user_data(username, elapsed_seconds, user_data)
    elif "Start" in entry:
        username = re.split(r"\s", entry)[1]
        user_data, active_sessions = initialize_user_data(
            username, active_sessions, user_data
        )
        active_sessions[username].append(timestamp)
    return user_data, active_sessions


def validate_log_entry(entry: str) -> bool:
    """Validates the integrity of each log entry."""
    parts = entry.strip().split()
    if len(parts) == 3:
        time, username, action = parts
        if re.match(r"\d{2}:\d{2}:\d{2}", time) and action in {"Start", "End"}:
            return True
    return False


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python script.py <log_file_path>")
        return 1

    filename = sys.argv[1]
    user_data: Dict[str, Dict[str, int]] = {}
    active_sessions: Dict[str, List[str]] = {}
    time_format = "%H:%M:%S"
    first_log_time = last_log_time = ""

    try:
        with open(filename, "r") as file:
            for entry in file:
                if validate_log_entry(entry):
                    if not first_log_time:
                        first_log_time = last_log_time = entry[:8]
                    last_log_time = entry[:8]
                    user_data, active_sessions = process_log_entry(
                        entry, user_data, time_format, active_sessions, first_log_time
                    )
    except IOError:
        print(f"Error reading file: {filename}")
        return 1

    user_data = finalize_sessions(
        active_sessions, last_log_time, user_data, time_format
    )
    output_results(user_data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
