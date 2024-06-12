import random

class Sidewinder:
    @staticmethod
    def on(grid):
        for row in grid.each_row():
            run = []
            for cell in row:
                run.append(cell)

                at_eastern_boundary = cell.east is None
                at_northern_boundary = cell.north is None

                should_close_out = at_eastern_boundary or (
                    not at_northern_boundary and random.choice([True, False])
                )

                if should_close_out:
                    member = random.choice(run)
                    if member.north:
                        member.link(member.north)
                    run.clear()
                else:
                    cell.link(cell.east)
        return grid
