def main():
    while True:
        s = input()
        n = len(s)
        ans = [' '] * n
        stk = []

        for i in range(n):
            if s[i] == '(':
                stk.append(i)
            elif s[i] == ')':
                if stk:
                    stk.pop()
                else:
                    ans[i] = '?'

        while stk:
            ans[stk.pop()] = 'x'

        print("".join(ans))

if __name__ == "__main__":
    main()
