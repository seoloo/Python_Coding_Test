## 내용

    - 000
        - input()은 무조건 문자열로 받음!
    
    # input()과 print()보다 sys.stdin.readline()과 sys.stdout.write() 사용하기

    # [뭐를(넣을값) for 어디에(변수) in 얼마나(반복대상)]

    # N, E = map(int, input().split()) : c++ -> int N,E; cin >> N >> E;
    # 각각에 int()를 적용해라
    # s, e, w = map(int, input().split()) : c++ -> int s, e, w; cin >> s >> e >> w;

    # Python에서는 배열과 리스트를 구별하지 않는다
    
    - 001
        - 리스트로 저장해야함
        - 각 값을 정수형으로 변환해 저장해야함
        - 한 자리씩 나누어 받으라는데 어떻게..?
        - Python에서 형변환 : int 형 변환 -> int(data), str 형 변환 -> str(data)

    -002
        - for 변수 in 반복가능한것.
            - 나는 for i in cnt:로 해서 실행이 안됨
        - 따라서 for i in range(cnt)로 해야함.
        - map(int, input().split()) 빨리 이 의미를 이해하고 기억해야할 듯.
        -