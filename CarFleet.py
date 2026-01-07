class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car=list(zip(position,speed))
        car.sort(reverse=True) # sort acording to the pos

        fleets=0
        prev_time=0

        for pos,sp in car:
            time=(target-pos)/sp
            if time >prev_time: #This car is slower than the fleet ahead →it cannot catch up → it becomes a new fleet
                fleets+=1
                prev_time=time #We update prev_time because this new fleet becomes the front barrier for all cars behind.
        return fleets 
        