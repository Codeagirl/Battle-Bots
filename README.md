# Bot Brawl

Can you make it to the end to become the ultimate battle bot Champion? Challenge an AI-controlled opponent or go head-to-head with a friend, upgrade your stats in the shop, and claim victory.

## Features

  -PVP and AI Modes: Battle locally against another player or test your luck against a custom-designed bot opponent.

  -Dynamic Turn-Based Combat: Tactical gameplay featuring standard attacks, dodging mechanics with luck-based success rates, and heavy-hitting double attacks.

  -Dynamic Attack Feedback: Variable damage multipliers with procedural combat narrative feedback based on total damage dealt.

  -In-Game Upgrade Shop: Earn coins from round victories to permanently upgrade health, attack power, and armor stats.

  -Round-Based Victory Tracking: Multi-round game progression tracking round wins and overall match results.

## Installation

To run the game, clone or download this repository from GitHub.

1. Make sure you have python or Visual Studio code downloaded on your device.

2. Open a terminal/command prompt in the project folder.

3. Run the main game file directly:

  '''
      python main.py
  '''


No external dependencies or virtual environments are required as the game runs using standard Python libraries (time, random, os).

## How to Play

When you launch the game, you'll be greeted by the main menu. From here, you can select option 1 to begin a battle.

Before starting, choose whether to play against a local friend (Option 1) or the AI Bot (Option 2).

During each turn, you can choose from three main combat actions:

1 - Attack: Deals variable damage based on your attack power minus enemy armor, multiplied by a random factor.

2 - Dodge: Offers a chance to evade incoming enemy damage and cause them to self-damage on a miss.

3 - Double Attack: Performs two attacks in a single turn. This powerful move can only be used once per match round.

Winning a battle awards you 10 coins, granting access to the shop where you can upgrade your robot's Health, Attack, and Armor attributes before moving on to the next round. The first player to win 2 rounds wins the match!

## Limitations

Terminal Environment: Screen clearing functionality relies on system-level OS calls (cls / clear), which may display unexpected artifacts in certain IDE-embedded consoles (such as PyCharm or VS Code integrated terminals). Running via standard Command Prompt, PowerShell, or macOS Terminal is recommended.

## Credits / Acknowledgments

Game developed by CodeaGirl, aka Violet.

Built using pure Python without third-party frameworks.
