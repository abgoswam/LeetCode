class LogEntry:
    def __init__(self, str):
        tokens = str.split(':')
        self.function_id = int(tokens[0])
        self.state = tokens[1]
        self.timestamp = int(tokens[2])

class QueueEntry:
    def __init__(self, id, timestamp):
        self.function_id = id
        self.timestamp = timestamp

class Solution:
    def exclusiveTime(self, n: int, logs):

        log_entries = []
        for item in logs:
            log_entry = LogEntry(item)
            log_entries.append(log_entry)


        queue = []
        running_time = {}

        for log_entry in log_entries:
            if log_entry.state == "start":
                if len(queue) == 0:
                    new_q_entry = QueueEntry(log_entry.function_id, log_entry.timestamp)
                else:
                    last_q_entry = queue[-1]
                    new_q_entry = QueueEntry(log_entry.function_id, log_entry.timestamp)
                    if last_q_entry.function_id in running_time:
                        running_time[last_q_entry.function_id] += (new_q_entry.timestamp - last_q_entry.timestamp)
                    else:
                        running_time[last_q_entry.function_id] = (new_q_entry.timestamp - last_q_entry.timestamp)

                queue.append(new_q_entry)
            else:
                last_q_entry = queue[-1]

                if last_q_entry.function_id in running_time:
                    running_time[last_q_entry.function_id] += (log_entry.timestamp - last_q_entry.timestamp) + 1
                else:
                    running_time[last_q_entry.function_id] = (log_entry.timestamp - last_q_entry.timestamp) + 1

                queue.pop()
                if len(queue) >= 1:
                    last_q_entry = queue[-1]
                    last_q_entry.timestamp = log_entry.timestamp + 1

        consolidated_running_time = []
        for id in range(n):
            if id in running_time:
                consolidated_running_time.append(running_time[id])
            else:
                consolidated_running_time.append(0)

        return consolidated_running_time

n = 2
logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]

s = Solution()
print(s.exclusiveTime(n, logs))
