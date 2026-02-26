import os
from datetime import datetime

KEY = "Key TSTFEED0300|7E3E|0400"
INPUT_FILE = "hblog.txt"
OUTPUT_FILE = "hb_test.log"


def analyze_heartbeat_log(input_file: str, output_file: str, key: str) -> None:

    if not os.path.exists(input_file):
        print(f"Файл '{input_file}' не знайдено! Поклади його в ту ж папку, що й скрипт.")
        return

    entries = []


    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            if key not in line:
                continue

            ts_index = line.find("Timestamp ")
            if ts_index == -1:
                continue

            time_str = line[ts_index + len("Timestamp "): ts_index + len("Timestamp ") + 8]

            try:
                timestamp = datetime.strptime(time_str, "%H:%M:%S")
            except ValueError:
                continue

            entries.append((timestamp, line.strip()))


    with open(output_file, "w", encoding="utf-8") as log:
        for i in range(1, len(entries)):
            prev_time, _ = entries[i - 1]
            curr_time, curr_line = entries[i]

            diff = (curr_time - prev_time).total_seconds()


            if diff < 0:
                diff += 24 * 60 * 60

            if 31 < diff < 33:
                log.write(
                    f"WARNING: heartbeat {int(diff)}s at {curr_time.strftime('%H:%M:%S')} | {curr_line}\n"
                )
            elif diff >= 33:
                log.write(
                    f"ERROR: heartbeat {int(diff)}s at {curr_time.strftime('%H:%M:%S')} | {curr_line}\n"
                )


if __name__ == "__main__":
    analyze_heartbeat_log(INPUT_FILE, OUTPUT_FILE, KEY)
    print("Аналіз heartbeat завершено. Результати збережено у hb_test.log")
