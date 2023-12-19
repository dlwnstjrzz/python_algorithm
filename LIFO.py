def dailyTemp(temperature):
    ans = [0] * len(temperature)
    stack = []
    for cur_day, cur_temp in enumerate(temperature):
        while stack and stack[-1][1] < cur_temp:
            prev_day, _ = stack.pop()
            ans[prev_day] = cur_day - prev_day
        stack.append((cur_day, cur_temp))
    return ans

print(dailyTemp([73,74,75,71,69,72,76,73]))
