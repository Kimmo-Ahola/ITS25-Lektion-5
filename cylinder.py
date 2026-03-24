from argparse import ArgumentParser

from math_functions import calculate_cylinder_volume

parser = ArgumentParser(description="Räkna ut volym på cylinder")

parser.add_argument(
    "radius", type=float, help="Radien för att räkna ut cylinderns volym"
)
parser.add_argument(
    "height", type=float, help="Höjden för att räkna ut cylinderns volym"
)

group = parser.add_mutually_exclusive_group()

# store_true = bool med False som default
# använder vi flaggan -q/-v blir den True
group.add_argument("-q", "--quiet", action="store_true")
group.add_argument("-v", "--verbose", action="store_true")


args = parser.parse_args()

if args.quiet:
    volume = calculate_cylinder_volume(args.radius, args.height)
    print(volume)
elif args.verbose:
    print(f"Variablerna är: radius: {args.radius}, height: {args.radius}")
    volume = calculate_cylinder_volume(args.radius, args.height)
    print(volume)
else:
    volume = calculate_cylinder_volume(args.radius, args.height)
    print(volume)
