## 클래스 선언 ##
class TreeNode:
    def __init__(self, key, book, author):
        self.key = key  # 검색 기준에 따라 설정된 키 값
        self.data = {"책": book, "작가": author}
        self.left = None
        self.right = None

## 데이터 준비 ##
bookAry = [
    {"책": "어린왕자", "작가": "쌩떽쥐베리"},
    {"책": "이방인", "작가": "까뮈"},
    {"책": "부활", "작가": "톨스토이"},
    {"책": "신곡", "작가": "단테"},
    {"책": "돈키호테", "작가": "세브반테스"},
    {"책": "동물농장", "작가": "조지오웰"},
    {"책": "데미안", "작가": "헤르만헤세"},
    {"책": "파우스트", "작가": "괴테"},
    {"책": "대지", "작가": "펄벅"}
]

## 검색 기준 설정 및 정렬 ##
def sort_and_build_tree(data, search_by):
    # 기준에 따라 정렬
    sorted_data = sorted(data, key=lambda x: x[search_by])
    
    # 균형 트리 생성
    return build_balanced_tree(sorted_data, search_by)

def build_balanced_tree(data, search_by):
    if not data:
        return None

    # 중간값을 루트로 설정
    mid = len(data) // 2
    root = TreeNode(data[mid][search_by], data[mid]["책"], data[mid]["작가"])

    # 왼쪽과 오른쪽 서브트리를 재귀적으로 생성
    root.left = build_balanced_tree(data[:mid], search_by)
    root.right = build_balanced_tree(data[mid + 1:], search_by)

    return root

## 검색 함수 ##
def search_tree(node, keyword):
    if node is None:
        return None
    if node.key == keyword:
        return node.data
    elif keyword < node.key:
        return search_tree(node.left, keyword)
    else:
        return search_tree(node.right, keyword)

## 실행 예시 ##
# 1. 책 제목으로 검색
search_by = "책"  # "작가"로 변경 가능
root = sort_and_build_tree(bookAry, search_by)

# 2. 검색 실행
keyword = "신곡"  # 검색할 제목 또는 작가 이름
result = search_tree(root, keyword)

if result:
    print(f"{search_by}: '{keyword}'의 검색 결과 -> {result}")
else:
    print(f"{search_by}: '{keyword}'를 찾을 수 없습니다.")
