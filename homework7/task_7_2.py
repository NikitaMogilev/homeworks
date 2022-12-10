def is_right_angle_triangle(a, b, c):
    result = {}
    if a + b < c:
        result['result'] = False
        result['description'] = "no such triangle exists"
    elif a**2 + b**2 != c**2:
        result['result'] = False
        result['description'] = "the triangle is not right-angled"
    else:
        result['result'] = True
        result['description'] = 'the triangle is right-angled'
    return result


triangle = is_right_angle_triangle(6, 8, 10)
print(triangle)
