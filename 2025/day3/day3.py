import time
from pathlib import Path

def max_number_from_digits(s: str, k: int) -> int:
    """Return the maximum integer obtainable by selecting k digits from s
    while preserving their relative order. Uses a monotonic stack in O(n).
    """
    n = len(s)
    if k >= n:
        return int(s)

    remove = n - k  # how many digits we can drop
    stack = []
    for ch in s:
        while stack and remove > 0 and stack[-1] < ch:
            stack.pop()
            remove -= 1
        stack.append(ch)

    # Still need to drop from the end
    return int("".join(stack[:k]))

def solve(input_list: list[str], k: int) -> int:
    """Calculate sum of max numbers with k digits for all inputs."""
    return sum(max_number_from_digits(line, k) for line in input_list)

def main() -> None:
    start_time = time.perf_counter()
    
    # Read input once
    input_path = Path(__file__).parent / "input.txt"
    input_list = [line.strip() for line in input_path.read_text().splitlines()]
    
    # Part 1
    print(solve(input_list, k=2))
    
    # Part 2
    print(solve(input_list, k=12))
    
    execution_time = time.perf_counter() - start_time
    print(f"Execution time: {execution_time:.9f} seconds")

if __name__ == "__main__":
    main()