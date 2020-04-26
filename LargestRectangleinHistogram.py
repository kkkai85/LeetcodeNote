heights = [2, 1, 5, 6, 2, 3]
heights = [1]
# heights = []
# heights = [1, 1]
# heights = [2, 4]
# heights = [9, 0]
heights = [2, 1, 2]

# if len(heights) == 0:
#     print(0)

# if len(heights) == 1:
#     print(heights)

# print(len(heights))

# ans = 0
# for mid in range(len(heights)):
#     k = 1
#     right = mid + 1 if mid + 1 < len(heights) else mid
#     left = mid - 1 if mid - 1 >= 0 else mid

#     print("mid = " + str(mid))
#     print("heigts = " + str(heights[mid]))
#     print("right = " + str(right))
#     print("left = " + str(left))

#     while right <= len(heights) - 1:
#         if heights[right] >= heights[mid] and right != mid:
#             k += 1
#             right += 1

#         else:
#             break

#     while left >= 0:
#         if heights[left] >= heights[mid] and mid != left:
#             k += 1
#             left -= 1

#         else:
#             break
    
#     print("right = " + str(right))
#     print("left = " + str(left))
#     print("k = " + str(k))

#     if ans < heights[mid] * k:
#         ans = heights[mid] * k

#     print("ans = " + str(ans))

# print(ans)

heights.append(0)
stack = [-1]
ans = 0
for i in range(len(heights)):
    print("i = " + str(i))
    while heights[i] < heights[stack[-1]]:
        h = heights[stack.pop()]
        print("h = " + str(h))
        w = i-stack[-1]-1
        print("w = " + str(w))
        ans = max(ans, h*w)
    stack.append(i)
    
print(ans)