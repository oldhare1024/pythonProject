Test = [
    {
        'q': '七十二小时',
        'a': '晶',
        'p': 5
    },
    {
        'q': '五十对耳朵',
        'a': '陌',
        'p': '5'
    }
]
for i, qa in enumerate(Test):
    guess = input('[第%02d题]%s:' % (i + 1, qa['q']))
    if guess == qa['a']:
        print(f'√+{qa["p"]}分')
    else:
        print(f'× {qa["a"]}')
