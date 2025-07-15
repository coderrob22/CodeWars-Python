def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    # Your code here.
    total = blue_start + red_start
    pulled = blue_pulled + red_pulled
    blue = blue_start - blue_pulled
    answer = blue/(total - pulled)
    return answer