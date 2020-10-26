from typing import List


def compute_area(A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
    def _is_rectangle_overlap(rec1: List[int], rec2: List[int]) -> bool:
        return not (rec1[2] <= rec2[0] or rec2[2] <= rec1[0] or rec1[1] >= rec2[3] or rec2[1] >= rec1[3])

    def _cal_inter(A, B, C, D, E, F, G, H):
        xa = max(A, E)
        ya = max(B, F)
        xb = min(C, G)
        yb = min(D, H)
        return (xb - xa) * (yb - ya)

    if _is_rectangle_overlap([A, B, C, D], [E, F, G, H]):
        return (C - A) * (D - B) + (G - E) * (H - F) - _cal_inter(A, B, C, D, E, F, G, H)

    return (C - A) * (D - B) + (G - E) * (H - F)


if __name__ == '__main__':
    print(compute_area(-3, 0, 3, 4, 0, -1, 9, 2))
