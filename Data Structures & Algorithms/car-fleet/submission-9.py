class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        sorted_pos = []

        for i in range(0, len(position)):
            sorted_pos.append((position[i], speed[i]))

        sorted_pos = sorted(sorted_pos, key=lambda tup: tup[0])

        slowest_time_ahead = 0
        fleet_counter = 0

        # calculate num of steps if ever below > top then merge
        for i in range(len(position) - 1, -1, -1):
            
            #sort for speeds
            pos = sorted_pos[i][0]
            velo = sorted_pos[i][1]

            # steps = ceil(distance rem / velo)
            steps = (target - pos)/velo

            if slowest_time_ahead < steps:
                fleet_counter+=1
                slowest_time_ahead = steps
           
                

        return fleet_counter




