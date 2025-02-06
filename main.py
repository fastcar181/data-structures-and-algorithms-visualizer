import random
import time

INVALID_RESPONSES = ["hey man that's not the input i asked you for!!!!", "ok buddy, you're not making any sense", "can we not do this man... enter something valid", "ENTER!!!SOMETHING!!!VALID!!!", "please enter something valid... any time today...", "yes please waste my time... i'll be here all day..."]

def selection_sort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
        print(arr)
        time.sleep(1)

def main():
    while True:
        try:
            length = int(input("Enter the length of the list to sort (-1 to exit): "))
            if length == -1: break
            arr = [random.randint(0, 100) for _ in range(length)]
            selection_sort(arr)
        except ValueError:
            print(INVALID_RESPONSES[random.randint(0, len(INVALID_RESPONSES)-1)])
    
    
if __name__ == "__main__":
    main()