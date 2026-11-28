def ft_count_harvest_recursive() -> None:
    total = int(input("Days until harvest: "))

    def count(first: int, last: int) -> None:
        if first > last:
            return
        elif first == last:
            print(f"Day {first}")
        else:
            mid = (first + last) // 2
            count(first, mid)
            count(mid + 1, last)
    count(1, total)
    print("Harvest time!")
