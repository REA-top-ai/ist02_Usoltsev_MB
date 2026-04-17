import  json


logs = [
    "2025-02-01 10:15:33|INFO|user=anna action=login status=success ip=10.0.0.1",
    "2025-02-01 10:17:10|ERROR|user=bob action=payment status=fail amount=120",
    "2025-02-01 10:20:01|INFO|user=anna action=logout status=success",
    "2025-02-01 10:22:45|WARNING|user=anna action=payment status=fail amount=300",
    "2025-02-01 10:30:12|ERROR|user=tom action=login status=fail ip=10.0.0.5"
]

#функция main

def logToDict (log: str) -> dict:
    parts = log.split('|')

    data = parts[0]
    level = parts[1]
    message = parts[2] #проверить бы длину списка, чтобы избежать out of range

    fields = message.split(" ")

    data = {"date": data, "level": level}

    for f in fields:
        key, value = f.split("=")
        try:
            value = int(value)
        except:
            pass
        data[key] = value

    return data


def parsedingLogs (logs: list) -> list:
    parsed_logs = []
    for log in logs:
        parsed_logs.append(logToDict(log))

    with open("logs.json", "w", encoding="utf-8") as f:
        json.dump(parsed_logs, f, ensure_ascii=False, indent=4)

    return parsed_logs


def filter_logs (logs: list, **filters) -> list:
    filtered_logs = []
    for log in logs:
        d = logToDict(log)
        flag = True
        for key, value in filters.items():
            if d[key] != value:
                flag = False
                break
        if flag:
            filtered_logs.append(d)
    return filtered_logs


def summer (parsed_logs: list, condition: str):
    if condition == "amount":
        summa = sum([log[condition] for log in parsed_logs if log.get(condition)])
        return summa

    result = {}
    for log in parsed_logs:
        if log.get(condition) and (log.get(condition) not in result.keys()):
            result[log[condition]] = 1
        elif log.get(condition) in result.keys():
            result[log[condition]] += 1
    return result

parsed_logs = parsedingLogs(logs)
print(parsed_logs)
print(filter_logs(logs, level="ERROR"))
print(summer(parsed_logs, "status"))
