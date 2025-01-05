class Solution:
    def checkOverlap(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:
        # radius, xCenter, yCenter
        # x1, x2, y1, y2
        # newX = radius + xCenter
        # newY = radius + yCenter

        if xCenter < x1:
            if (yCenter >= y1) and (yCenter <= y2 + radius):
                if radius + xCenter >= x1:
                    return True

            if yCenter >= y1 - radius and yCenter <= y2:
                if radius + xCenter >= x1:
                    return True

        elif xCenter > x2:
            if yCenter >= y1 and yCenter <= y2 + radius:
                if xCenter - radius <= x2:
                    return True

            if yCenter >= y1 - radius and yCenter <= y2:
                if xCenter - radius <= x2:
                    return True

        else:
            if yCenter >= y1 and yCenter <= y2 + radius:
                return True

            if yCenter >= y1 - radius and yCenter <= y2:
                return True

        return False
