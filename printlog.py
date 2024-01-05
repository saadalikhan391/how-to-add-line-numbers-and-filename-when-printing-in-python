from rich.console import Console

console = Console()

console.log("Starting loop.", style="red")

for i in range(100):
    # Do something
    # print(f"Processing loop 1: {i}")
    pass

console.log(f"In between loops {i}", style="bright_yellow")

for j in range(200):
    # Do something else
    # print(f"Processing loop 2: {j}")

    pass

console.log(f"Finished! {j}", style="green")