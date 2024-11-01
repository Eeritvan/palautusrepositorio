from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from rich import print
from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    console = Console()
    console.print("NHL statistics by nationality", style="i")
    seasons = ["2018-19",
               "2019-20",
               "2020-21",
               "2021-22",
               "2022-23",
               "2023-24",
               "2024-25"]
    season = Prompt.ask("Select season", choices=seasons)

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    
    while True:
        nationalities = ["AUT",
                         "CZE",
                         "AUS",
                         "SWE",
                         "GER",
                         "DEN",
                         "SUI",
                         "SVK",
                         "NOR",
                         "RUS",
                         "CAN",
                         "LAT",
                         "BLR",
                         "SLO",
                         "USA",
                         "FIN",
                         "GBR"]
        nationality = Prompt.ask("Select nationality", choices=nationalities)
        players = stats.top_scorers_by_nationality(nationality)

        table = Table(title=f"Top scorers of {nationality} season {season}")
        table.add_column("name", justify="left", style="cyan", no_wrap=True)
        table.add_column("team", style="magenta")
        table.add_column("goals", style="green")
        table.add_column("assists", style="green")
        table.add_column("points", style="green")

        players.sort(reverse=True, key=lambda player:player.assists + player.goals)

        for player in players:
            table.add_row(player.name,
                          player.team,
                          str(player.goals),
                          str(player.assists),
                          str(player.goals+player.assists))
                
        console.print(table)


if __name__ == "__main__":
    main()