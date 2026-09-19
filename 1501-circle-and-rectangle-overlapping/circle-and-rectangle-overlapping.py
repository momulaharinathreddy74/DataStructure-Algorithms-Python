class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        
        # a=((x2-x1)**2+(y2-y1)**2)**0.5
        # xm=(x1+x2)//2
        # ym=(y1+y2)//2
        # dis=((xCenter-xm)**2+(yCenter-ym)**2)**0.5
        # if dis<radius+a/2:
        #     return True
        # else:
        #     return False
        closestX = max(x1, min(xCenter, x2))
        closestY = max(y1, min(yCenter, y2))

        dx = xCenter - closestX
        dy = yCenter - closestY

        return dx * dx + dy * dy <= radius * radius