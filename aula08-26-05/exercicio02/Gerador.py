"""
Código utilizado para fins didáticos no Curso de Sistemas de Informação da Universidade Federal de Santa Maria - Campus Frederico Westphalen
Autor: Prof. Dr. Joel da Silva

Este módulo implementa um gerador de nomes, sobrenomes e idades de pessoas

"""

import random

class Gerador:
    '''
    A Classe Gerador contem um vetor de nomes e outro de sobrenomes, que são utilizados para gerar nomes fictícios aleatoriamente
    '''
    nomes = [
    "Mary",
    "Patricia",
    "Linda",
    "Barbara",
    "Elizabeth",
    "Jennifer",
    "Maria",
    "Susan",
    "Margaret",
    "Dorothy",
    "Lisa",
    "Nancy",
    "Karen",
    "Betty",
    "Helen",
    "Sandra",
    "Donna",
    "Carol",
    "Ruth",
    "Sharon",
    "Michelle",
    "Laura",
    "Sarah",
    "Kimberly",
    "Deborah",
    "Jessica",
    "Shirley",
    "Cynthia",
    "Angela",
    "Melissa",
    "Brenda",
    "Amy",
    "Anna",
    "Rebecca",
    "Virginia",
    "Kathleen",
    "Pamela",
    "Martha",
    "Debra",
    "Amanda",
    "Stephanie",
    "Carolyn",
    "Christine",
    "Marie",
    "Janet",
    "Catherine",
    "Frances",
    "Ann",
    "Joyce",
    "Diane",
    "Alice",
    "Julie",
    "Heather",
    "Teresa",
    "Doris",
    "Gloria",
    "Evelyn",
    "Jean",
    "Cheryl",
    "Mildred",
    "Katherine",
    "Joan",
    "Ashley",
    "Judith",
    "Rose",
    "Janice",
    "Kelly",
    "Nicole",
    "Judy",
    "Christina",
    "Kathy",
    "Theresa",
    "Beverly",
    "Denise",
    "Tammy",
    "Irene",
    "Jane",
    "Lori",
    "Rachel",
    "Marilyn",
    "Andrea",
    "Kathryn",
    "Louise",
    "Sara",
    "Anne",
    "Jacqueline",
    "Wanda",
    "Bonnie",
    "Julia",
    "Ruby",
    "Lois",
    "Tina",
    "Phyllis",
    "Norma",
    "Paula",
    "Diana",
    "Annie",
    "Lillian",
    "Emily",
    "Robin",
    "Peggy",
    "Crystal",
    "Gladys",
    "Rita",
    "Dawn",
    "Connie",
    "Florence",
    "Tracy",
    "Edna",
    "Tiffany",
    "Carmen",
    "Rosa",
    "Cindy",
    "Grace",
    "Wendy",
    "Victoria",
    "Edith",
    "Kim",
    "Sherry",
    "Sylvia",
    "Josephine",
    "Thelma",
    "Shannon",
    "Sheila",
    "Ethel",
    "Ellen",
    "Elaine",
    "Marjorie",
    "Carrie",
    "Charlotte",
    "Monica",
    "Esther",
    "Pauline",
    "Emma",
    "Juanita",
    "Anita",
    "Rhonda",
    "Hazel",
    "Amber",
    "Eva",
    "Debbie",
    "April",
    "Leslie",
    "Clara",
    "Lucille",
    "Jamie",
    "Joanne",
    "Eleanor",
    "Valerie",
    "Danielle",
    "Megan",
    "Alicia",
    "Suzanne",
    "Michele",
    "Gail",
    "Bertha",
    "Darlene",
    "Veronica",
    "Jill",
    "Erin",
    "Geraldine",
    "Lauren",
    "Cathy",
    "Joann",
    "Lorraine",
    "Lynn",
    "Sally",
    "Regina",
    "Erica",
    "Beatrice",
    "Dolores",
    "Bernice",
    "Audrey",
    "Yvonne",
    "Annette",
    "June",
    "Samantha",
    "Marion",
    "Dana",
    "Stacy",
    "Ana",
    "Renee",
    "Ida",
    "Vivian",
    "Roberta",
    "Holly",
    "Brittany",
    "Melanie",
    "Loretta",
    "Yolanda",
    "Jeanette",
    "Laurie",
    "Katie",
    "Kristen",
    "Vanessa",
    "Alma",
    "Sue",
    "Elsie",
    "Beth",
    "Jeanne",
    "Vicki",
    "Carla",
    "Tara",
    "Rosemary",
    "Eileen",
    "Terri",
    "Gertrude",
    "Lucy",
    "Tonya",
    "Ella",
    "Stacey",
    "Wilma",
    "Gina",
    "Kristin",
    "Jessie",
    "Natalie",
    "Agnes",
    "Vera",
    "Willie",
    "Charlene",
    "Bessie",
    "Delores",
    "Melinda",
    "Pearl",
    "Arlene",
    "Maureen",
    "Colleen",
    "Allison",
    "Tamara",
    "Joy",
    "Georgia",
    "Constance",
    "Lillie",
    "Claudia",
    "Jackie",
    "Marcia",
    "Tanya",
    "Nellie",
    "Minnie",
    "Marlene",
    "Heidi",
    "Glenda",
    "Lydia",
    "Viola",
    "Courtney",
    "Marian",
    "Stella",
    "Caroline",
    "Dora",
    "Jo",
    "Vickie",
    "Mattie",
    "Terry",
    "Maxine",
    "Irma",
    "Mabel",
    "Marsha",
    "Myrtle",
    "Lena",
    "Christy",
    "Deanna",
    "Patsy",
    "Hilda",
    "Gwendolyn",
    "Jennie",
    "Nora",
    "Margie",
    "Nina",
    "Cassandra",
    "Leah",
    "Penny",
    "Kay",
    "Priscilla",
    "Naomi",
    "Carole",
    "Brandy",
    "Olga",
    "Billie",
    "Dianne",
    "Tracey",
    "Leona",
    "Jenny",
    "Felicia",
    "Sonia",
    "Miriam",
    "Velma",
    "Becky",
    "Bobbie",
    "Violet",
    "Kristina",
    "Toni",
    "Misty",
    "Mae",
    "Shelly",
    "Daisy",
    "Ramona",
    "Sherri",
    "Erika",
    "James",
    "John",
    "Robert",
    "Michael",
    "William",
    "David",
    "Richard",
    "Charles",
    "Joseph",
    "Thomas",
    "Christopher",
    "Daniel",
    "Paul",
    "Mark",
    "Donald",
    "George",
    "Kenneth",
    "Steven",
    "Edward",
    "Brian",
    "Ronald",
    "Anthony",
    "Kevin",
    "Jason",
    "Matthew",
    "Gary",
    "Timothy",
    "Jose",
    "Larry",
    "Jeffrey",
    "Frank",
    "Scott",
    "Eric",
    "Stephen",
    "Andrew",
    "Raymond",
    "Gregory",
    "Joshua",
    "Jerry",
    "Dennis",
    "Walter",
    "Patrick",
    "Peter",
    "Harold",
    "Douglas",
    "Henry",
    "Carl",
    "Arthur",
    "Ryan",
    "Roger",
    "Joe",
    "Juan",
    "Jack",
    "Albert",
    "Jonathan",
    "Justin",
    "Terry",
    "Gerald",
    "Keith",
    "Samuel",
    "Willie",
    "Ralph",
    "Lawrence",
    "Nicholas",
    "Roy",
    "Benjamin",
    "Bruce",
    "Brandon",
    "Adam",
    "Harry",
    "Fred",
    "Wayne",
    "Billy",
    "Steve",
    "Louis",
    "Jeremy",
    "Aaron",
    "Randy",
    "Howard",
    "Eugene",
    "Carlos",
    "Russell",
    "Bobby",
    "Victor",
    "Martin",
    "Ernest",
    "Phillip",
    "Todd",
    "Jesse",
    "Craig",
    "Alan",
    "Shawn",
    "Clarence",
    "Sean",
    "Philip",
    "Chris",
    "Johnny",
    "Earl",
    "Jimmy",
    "Antonio",
    "Danny",
    "Bryan",
    "Tony",
    "Luis",
    "Mike",
    "Stanley",
    "Leonard",
    "Nathan",
    "Dale",
    "Manuel",
    "Rodney",
    "Curtis",
    "Norman",
    "Allen",
    "Marvin",
    "Vincent",
    "Glenn",
    "Jeffery",
    "Travis",
    "Jeff",
    "Chad",
    "Jacob",
    "Lee",
    "Melvin",
    "Alfred",
    "Kyle",
    "Francis",
    "Bradley",
    "Jesus",
    "Herbert",
    "Frederick",
    "Ray",
    "Joel",
    "Edwin",
    "Don",
    "Eddie",
    "Ricky",
    "Troy",
    "Randall",
    "Barry",
    "Alexander",
    "Bernard",
    "Mario",
    "Leroy",
    "Francisco",
    "Marcus",
    "Micheal",
    "Theodore",
    "Clifford",
    "Miguel",
    "Oscar",
    "Jay",
    "Jim",
    "Tom",
    "Calvin",
    "Alex",
    "Jon",
    "Ronnie",
    "Bill",
    "Lloyd",
    "Tommy",
    "Leon",
    "Derek",
    "Warren",
    "Darrell",
    "Jerome",
    "Floyd",
    "Leo",
    "Alvin",
    "Tim",
    "Wesley",
    "Gordon",
    "Dean",
    "Greg",
    "Jorge",
    "Dustin",
    "Pedro",
    "Derrick",
    "Dan",
    "Lewis",
    "Zachary",
    "Corey",
    "Herman",
    "Maurice",
    "Vernon",
    "Roberto",
    "Clyde",
    "Glen",
    "Hector",
    "Shane",
    "Ricardo",
    "Sam",
    "Rick",
    "Lester",
    "Brent",
    "Ramon",
    "Charlie",
    "Tyler",
    "Gilbert",
    "Gene",
    "Marc",
    "Reginald",
    "Ruben",
    "Brett",
    "Angel",
    "Nathaniel",
    "Rafael",
    "Leslie",
    "Edgar",
    "Milton",
    "Raul",
    "Ben",
    "Chester",
    "Cecil",
    "Duane",
    "Franklin",
    "Andre",
    "Elmer",
    "Brad",
    "Gabriel",
    "Ron",
    "Mitchell",
    "Roland",
    "Arnold",
    "Harvey",
    "Jared",
    "Adrian",
    "Karl",
    "Cory",
    "Claude",
    "Erik",
    "Darryl",
    "Jamie",
    "Neil",
    "Jessie",
    "Christian",
    "Javier",
    "Fernando",
    "Clinton",
    "Ted",
    "Mathew",
    "Tyrone",
    "Darren",
    "Lonnie",
    "Lance",
    "Cody",
    "Julio",
    "Kelly",
    "Kurt",
    "Allan",
    "Nelson",
    "Guy",
    "Clayton",
    "Hugh",
    "Max",
    "Dwayne",
    "Dwight",
    "Armando",
    "Felix",
    "Jimmie",
    "Everett",
    "Jordan",
    "Ian",
    "Wallace",
    "Ken",
    "Bob",
    "Jaime",
    "Casey",
    "Alfredo",
    "Alberto",
    "Dave",
    "Ivan",
    "Johnnie",
    "Sidney",
    "Byron",
    "Julian",
    "Isaac",
    "Morris",
    "Clifton",
    "Willard",
    "Daryl",
    "Ross",
    "Virgil",
    "Andy",
    "Marshall",
    "Salvador",
    "Perry",
    "Kirk",
    "Sergio",
    "Marion",
    "Tracy",
    "Seth",
    "Kent",
    "Terrance",
    "Rene",
    "Eduardo",
    "Terrence",
    "Enrique",
    "Freddie",
    "Wade",
    "Austin",
    "Penelope",
    "Nick",
    "Ed",
    "Jennifer",
    "Johnny",
    "Bette",
    "Grace",
    "Matthew",
    "Joe",
    "Christian",
    "Zero",
    "Karl",
    "Uma",
    "Vivien",
    "Cuba",
    "Fred",
    "Helen",
    "Dan",
    "Bob",
    "Lucille",
    "Kirsten",
    "Elvis",
    "Sandra",
    "Cameron",
    "Kevin",
    "Rip",
    "Julia",
    "Woody",
    "Alec",
    "Sandra",
    "Sissy",
    "Tim",
    "Milla",
    "Audrey",
    "Judy",
    "Burt",
    "Val",
    "Tom",
    "Goldie",
    "Johnny",
    "Jodie",
    "Tom",
    "Kirk",
    "Nick",
    "Reese",
    "Parker",
    "Julia",
    "Frances",
    "Anne",
    "Natalie",
    "Gary",
    "Carmen",
    "Mena",
    "Penelope",
    "Fay",
    "Dan",
    "Jude",
    "Christian",
    "Dustin",
    "Henry",
    "Christian",
    "Jayne",
    "Cameron",
    "Ray",
    "Angela",
    "Mary",
    "Jessica",
    "Rip",
    "Kenneth",
    "Michelle",
    "Adam",
    "Sean",
    "Gary",
    "Milla",
    "Burt",
    "Angelina",
    "Cary",
    "Groucho",
    "Mae",
    "Ralph",
    "Scarlett",
    "Woody",
    "Ben",
    "James",
    "Minnie",
    "Greg",
    "Spencer",
    "Kenneth",
    "Charlize",
    "Sean",
    "Christopher",
    "Kirsten",
    "Ellen",
    "Kenneth",
    "Daryl",
    "Gene",
    "Meg",
    "Chris",
    "Jim",
    "Spencer",
    "Susan",
    "Walter",
    "Matthew",
    "Penelope",
    "Sidney",
    "Groucho",
    "Gina",
    "Warren",
    "Sylvester",
    "Susan",
    "Cameron",
    "Russell",
    "Morgan",
    "Morgan",
    "Harrison",
    "Dan",
    "Renee",
    "Cuba",
    "Warren",
    "Penelope",
    "Liza",
    "Salma",
    "Julianne",
    "Scarlett",
    "Albert",
    "Frances",
    "Kevin",
    "Cate",
    "Daryl",
    "Greta",
    "Jane",
    "Adam",
    "Richard",
    "Gene",
    "Rita",
    "Ed",
    "Morgan",
    "Lucille",
    "Ewan",
    "Whoopi",
    "Cate",
    "Jada",
    "River",
    "Angela",
    "Kim",
    "Albert",
    "Fay",
    "Emily",
    "Russell",
    "Jayne",
    "Geoffrey",
    "Ben",
    "Minnie",
    "Meryl",
    "Ian",
    "Fay",
    "Greta",
    "Vivien",
    "Laura",
    "Chris",
    "Harvey",
    "Oprah",
    "Christopher",
    "Humphrey",
    "Al",
    "Nick",
    "Laurence",
    "Will",
    "Kenneth",
    "Mena",
    "Olympia",
    "Groucho",
    "Alan",
    "Michael",
    "William",
    "Jon",
    "Gene",
    "Lisa",
    "Ed",
    "Jeff",
    "Matthew",
    "Debbie",
    "Russell",
    "Humphrey",
    "Michael",
    "Julia",
    "Renee",
    "Rock",
    "Cuba",
    "Audrey",
    "Gregory",
    "John",
    "Burt",
    "Meryl",
    "Jayne",
    "Bela",
    "Reese",
    "Mary",
    "Julia",
    "Thora",
    "Mike",
    "Jon",
    "Maria",
    "João",
    "Maria",
    "Neusa",
    "Roque",
    "Patrício",
    "Juca",
    "Josiane",
    "Josefa",
    "Mauro",
    "Jonas",
    "Claudio",
    "Miguel",
    "Davi",
    "Manoel",
    "Emanoel",
    "Lauro",
    "Laura",
    "Jean",
    "Débora",
    "Joel",
    "Miriam",
    "Gabrielly",
    "Wilmo"]

    sobrenomes = [
    "Smith",
    "Johnson",
    "Williams",
    "Jones",
    "Brown",
    "Davis",
    "Miller",
    "Wilson",
    "Moore",
    "Taylor",
    "Anderson",
    "Thomas",
    "Jackson",
    "White",
    "Harris",
    "Martin",
    "Thompson",
    "Garcia",
    "Martinez",
    "Robinson",
    "Clark",
    "Rodriguez",
    "Lewis",
    "Lee",
    "Walker",
    "Hall",
    "Allen",
    "Young",
    "Hernandez",
    "King",
    "Wright",
    "Lopez",
    "Hill",
    "Scott",
    "Green",
    "Adams",
    "Baker",
    "Gonzalez",
    "Nelson",
    "Carter",
    "Mitchell",
    "Perez",
    "Roberts",
    "Turner",
    "Phillips",
    "Campbell",
    "Parker",
    "Evans",
    "Edwards",
    "Collins",
    "Stewart",
    "Sanchez",
    "Morris",
    "Rogers",
    "Reed",
    "Cook",
    "Morgan",
    "Bell",
    "Murphy",
    "Bailey",
    "Rivera",
    "Cooper",
    "Richardson",
    "Cox",
    "Howard",
    "Ward",
    "Torres",
    "Peterson",
    "Gray",
    "Ramirez",
    "James",
    "Watson",
    "Brooks",
    "Kelly",
    "Sanders",
    "Price",
    "Bennett",
    "Wood",
    "Barnes",
    "Ross",
    "Henderson",
    "Coleman",
    "Jenkins",
    "Perry",
    "Powell",
    "Long",
    "Patterson",
    "Hughes",
    "Flores",
    "Washington",
    "Butler",
    "Simmons",
    "Foster",
    "Gonzales",
    "Bryant",
    "Alexander",
    "Russell",
    "Griffin",
    "Diaz",
    "Hayes",
    "Myers",
    "Ford",
    "Hamilton",
    "Graham",
    "Sullivan",
    "Wallace",
    "Woods",
    "Cole",
    "West",
    "Jordan",
    "Owens",
    "Reynolds",
    "Fisher",
    "Ellis",
    "Harrison",
    "Gibson",
    "Mcdonald",
    "Cruz",
    "Marshall",
    "Ortiz",
    "Gomez",
    "Murray",
    "Freeman",
    "Wells",
    "Webb",
    "Simpson",
    "Stevens",
    "Tucker",
    "Porter",
    "Hunter",
    "Hicks",
    "Crawford",
    "Henry",
    "Boyd",
    "Mason",
    "Morales",
    "Kennedy",
    "Warren",
    "Dixon",
    "Ramos",
    "Reyes",
    "Burns",
    "Gordon",
    "Shaw",
    "Holmes",
    "Rice",
    "Robertson",
    "Hunt",
    "Black",
    "Daniels",
    "Palmer",
    "Mills",
    "Nichols",
    "Grant",
    "Knight",
    "Ferguson",
    "Rose",
    "Stone",
    "Hawkins",
    "Dunn",
    "Perkins",
    "Hudson",
    "Spencer",
    "Gardner",
    "Stephens",
    "Payne",
    "Pierce",
    "Berry",
    "Matthews",
    "Arnold",
    "Wagner",
    "Willis",
    "Ray",
    "Watkins",
    "Olson",
    "Carroll",
    "Duncan",
    "Snyder",
    "Hart",
    "Cunningham",
    "Bradley",
    "Lane",
    "Andrews",
    "Ruiz",
    "Harper",
    "Fox",
    "Riley",
    "Armstrong",
    "Carpenter",
    "Weaver",
    "Greene",
    "Lawrence",
    "Elliott",
    "Chavez",
    "Sims",
    "Austin",
    "Peters",
    "Kelley",
    "Franklin",
    "Lawson",
    "Fields",
    "Gutierrez",
    "Ryan",
    "Schmidt",
    "Carr",
    "Vasquez",
    "Castillo",
    "Wheeler",
    "Chapman",
    "Oliver",
    "Montgomery",
    "Richards",
    "Williamson",
    "Johnston",
    "Banks",
    "Meyer",
    "Bishop",
    "Mccoy",
    "Howell",
    "Alvarez",
    "Morrison",
    "Hansen",
    "Fernandez",
    "Garza",
    "Harvey",
    "Little",
    "Burton",
    "Stanley",
    "Nguyen",
    "George",
    "Jacobs",
    "Reid",
    "Kim",
    "Fuller",
    "Lynch",
    "Dean",
    "Gilbert",
    "Garrett",
    "Romero",
    "Welch",
    "Larson",
    "Frazier",
    "Burke",
    "Hanson",
    "Day",
    "Mendoza",
    "Moreno",
    "Bowman",
    "Medina",
    "Fowler",
    "Brewer",
    "Hoffman",
    "Carlson",
    "Silva",
    "Pearson",
    "Holland",
    "Douglas",
    "Fleming",
    "Jensen",
    "Vargas",
    "Byrd",
    "Davidson",
    "Hopkins",
    "May",
    "Terry",
    "Herrera",
    "Wade",
    "Soto",
    "Walters",
    "Curtis",
    "Neal",
    "Caldwell",
    "Lowe",
    "Jennings",
    "Barnett",
    "Graves",
    "Jimenez",
    "Horton",
    "Shelton",
    "Barrett",
    "Obrien",
    "Castro",
    "Sutton",
    "Gregory",
    "Mckinney",
    "Lucas",
    "Miles",
    "Craig",
    "Rodriquez",
    "Chambers",
    "Holt",
    "Lambert",
    "Fletcher",
    "Watts",
    "Bates",
    "Hale",
    "Rhodes",
    "Pena",
    "Gannon",
    "Farnsworth",
    "Baughman",
    "Silverman",
    "Satterfield",
    "Royal",
    "Mccrary",
    "Kowalski",
    "Joy",
    "Grigsby",
    "Greco",
    "Cabral",
    "Trout",
    "Rinehart",
    "Mahon",
    "Linton",
    "Gooden",
    "Curley",
    "Baugh",
    "Wyman",
    "Weiner",
    "Schwab",
    "Schuler",
    "Morrissey",
    "Mahan",
    "Coy",
    "Bunn",
    "Andrew",
    "Thrasher",
    "Spear",
    "Waggoner",
    "Shelley",
    "Robert",
    "Qualls",
    "Purdy",
    "Mcwhorter",
    "Mauldin",
    "Mark",
    "Jordon",
    "Gilman",
    "Perryman",
    "Newsom",
    "Menard",
    "Martino",
    "Graf",
    "Billingsley",
    "Artis",
    "Simpkins",
    "Salisbury",
    "Quintanilla",
    "Gilliland",
    "Fraley",
    "Foust",
    "Crouse",
    "Scarborough",
    "Ngo",
    "Grissom",
    "Fultz",
    "Rico",
    "Marlow",
    "Markham",
    "Madrigal",
    "Lawton",
    "Barfield",
    "Whiting",
    "Varney",
    "Schwarz",
    "Huey",
    "Gooch",
    "Arce",
    "Wheat",
    "Truong",
    "Poulin",
    "Mackenzie",
    "Leone",
    "Hurtado",
    "Selby",
    "Gaither",
    "Fortner",
    "Culpepper",
    "Coughlin",
    "Brinson",
    "Boudreau",
    "Barkley",
    "Bales",
    "Stepp",
    "Holm",
    "Tan",
    "Schilling",
    "Morrell",
    "Kahn",
    "Heaton",
    "Gamez",
    "Douglass",
    "Causey",
    "Brothers",
    "Turpin",
    "Shanks",
    "Schrader",
    "Meek",
    "Isom",
    "Hardison",
    "Carranza",
    "Yanez",
    "Way",
    "Scroggins",
    "Schofield",
    "Runyon",
    "Ratcliff",
    "Murrell",
    "Moeller",
    "Irby",
    "Currier",
    "Butterfield",
    "Yee",
    "Ralston",
    "Pullen",
    "Pinson",
    "Estep",
    "East",
    "Carbone",
    "Lance",
    "Hawks",
    "Ellington",
    "Casillas",
    "Spurlock",
    "Sikes",
    "Motley",
    "Mccartney",
    "Kruger",
    "Isbell",
    "Houle",
    "Francisco",
    "Burk",
    "Bone",
    "Tomlin",
    "Shelby",
    "Quigley",
    "Neumann",
    "Lovelace",
    "Fennell",
    "Colby",
    "Cheatham",
    "Bustamante",
    "Skidmore",
    "Hidalgo",
    "Forman",
    "Culp",
    "Bowens",
    "Betancourt",
    "Aquino",
    "Robb",
    "Rea",
    "Milner",
    "Martel",
    "Gresham",
    "Wiles",
    "Ricketts",
    "Gavin",
    "Dowd",
    "Collazo",
    "Bostic",
    "Blakely",
    "Sherrod",
    "Power",
    "Kenyon",
    "Gandy",
    "Ebert",
    "Deloach",
    "Cary",
    "Bull",
    "Allard",
    "Sauer",
    "Robins",
    "Olivares",
    "Gillette",
    "Chestnut",
    "Bourque",
    "Paine",
    "Lyman",
    "Hite",
    "Hauser",
    "Devore",
    "Crawley",
    "Chapa",
    "Vu",
    "Tobias",
    "Talbert",
    "Poindexter",
    "Millard",
    "Meador",
    "Mcduffie",
    "Mattox",
    "Kraus",
    "Harkins",
    "Choate",
    "Bess",
    "Wren",
    "Sledge",
    "Sanborn",
    "Outlaw",
    "Kinder",
    "Geary",
    "Cornwell",
    "Barclay",
    "Adam",
    "Abney",
    "Seward",
    "Rhoads",
    "Howland",
    "Fortier",
    "Easter",
    "Benner",
    "Vines",
    "Tubbs",
    "Troutman",
    "Rapp",
    "Noe",
    "Mccurdy",
    "Harder",
    "Deluca",
    "Westmoreland",
    "South",
    "Havens",
    "Guajardo",
    "Ely",
    "Clary",
    "Seal",
    "Meehan",
    "Herzog",
    "Guillen",
    "Ashcraft",
    "Waugh",
    "Renner",
    "Milam",
    "Jung",
    "Elrod",
    "Churchill",
    "Buford",
    "Breaux",
    "Bolin",
    "Asher",
    "Windham",
    "Tirado",
    "Pemberton",
    "Nolen",
    "Noland",
    "Knott",
    "Emmons",
    "Cornish",
    "Christenson",
    "Brownlee",
    "Barbee",
    "Waldrop",
    "Pitt",
    "Olvera",
    "Lombardi",
    "Gruber",
    "Gaffney",
    "Eggleston",
    "Banda",
    "Archuleta",
    "Still",
    "Slone",
    "Prewitt",
    "Pfeiffer",
    "Nettles",
    "Mena",
    "Mcadams",
    "Henning",
    "Gardiner",
    "Cromwell",
    "Chisholm",
    "Burleson",
    "Box",
    "Vest",
    "Oglesby",
    "Mccarter",
    "Malcolm",
    "Lumpkin",
    "Larue",
    "Grey",
    "Wofford",
    "Vanhorn",
    "Thorn",
    "Teel",
    "Swafford",
    "Stclair",
    "Stanfield",
    "Ocampo",
    "Herrmann",
    "Hannon",
    "Arsenault",
    "Roush",
    "Mcalister",
    "Hiatt",
    "Gunderson",
    "Forsythe",
    "Duggan",
    "Delvalle",
    "Cintron",
    "Guiness",
    "Wahlberg",
    "Chase",
    "Davis",
    "Lollobrigida",
    "Nicholson",
    "Mostel",
    "Johansson",
    "Swank",
    "Gable",
    "Cage",
    "Berry",
    "Wood",
    "Bergen",
    "Olivier",
    "Costner",
    "Voight",
    "Torn",
    "Fawcett",
    "Tracy",
    "Paltrow",
    "Marx",
    "Kilmer",
    "Streep",
    "Bloom",
    "Crawford",
    "Mcqueen",
    "Hoffman",
    "Wayne",
    "Peck",
    "Sobieski",
    "Hackman",
    "Peck",
    "Olivier",
    "Dean",
    "Dukakis",
    "Bolger",
    "Mckellen",
    "Brody",
    "Cage",
    "Degeneres",
    "Miranda",
    "Jovovich",
    "Stallone",
    "Kilmer",
    "Goldberg",
    "Barrymore",
    "Day-Lewis",
    "Cronyn",
    "Hopkins",
    "Phoenix",
    "Hunt",
    "Temple",
    "Pinkett",
    "Kilmer",
    "Harris",
    "Cruise",
    "Akroyd",
    "Tautou",
    "Berry",
    "Neeson",
    "Neeson",
    "Wray",
    "Johansson",
    "Hudson",
    "Tandy",
    "Bailey",
    "Winslet",
    "Paltrow",
    "Mcconaughey",
    "Grant",
    "Williams",
    "Penn",
    "Keitel",
    "Posey",
    "Astaire",
    "Mcconaughey",
    "Sinatra",
    "Hoffman",
    "Cruz",
    "Damon",
    "Jolie",
    "Willis",
    "Pitt",
    "Zellweger",
    "Chaplin",
    "Peck",
    "Pesci",
    "Dench",
    "Guiness",
    "Berry",
    "Akroyd",
    "Presley",
    "Torn",
    "Wahlberg",
    "Willis",
    "Hawke",
    "Bridges",
    "Mostel",
    "Depp",
    "Davis",
    "Torn",
    "Leigh",
    "Cronyn",
    "Crowe",
    "Dunst",
    "Degeneres",
    "Nolte",
    "Dern",
    "Davis",
    "Zellweger",
    "Bacall",
    "Hopkins",
    "Mcdormand",
    "Bale",
    "Streep",
    "Tracy",
    "Allen",
    "Jackman",
    "Monroe",
    "Bergman",
    "Nolte",
    "Dench",
    "Bening",
    "Nolte",
    "Tomei",
    "Garland",
    "Mcqueen",
    "Crawford",
    "Keitel",
    "Jackman",
    "Hopper",
    "Penn",
    "Hopkins",
    "Reynolds",
    "Mansfield",
    "Williams",
    "Dee",
    "Gooding",
    "Hurt",
    "Harris",
    "Ryder",
    "Dean",
    "Witherspoon",
    "Allen",
    "Johansson",
    "Winslet",
    "Dee",
    "Temple",
    "Nolte",
    "Heston",
    "Harris",
    "Kilmer",
    "Gibson",
    "Tandy",
    "Wood",
    "Malden",
    "Basinger",
    "Brody",
    "Depp",
    "Hope",
    "Kilmer",
    "West",
    "Willis",
    "Garland",
    "Degeneres",
    "Bullock",
    "Wilson",
    "Hoffman",
    "Hopper",
    "Pfeiffer",
    "Williams",
    "Dreyfuss",
    "Bening",
    "Hackman",
    "Chase",
    "Mckellen",
    "Monroe",
    "Guiness",
    "Silverstone",
    "Carrey",
    "Akroyd",
    "Close",
    "Garland",
    "Bolger",
    "Zellweger",
    "Ball",
    "Dukakis",
    "Birch",
    "Bailey",
    "Gooding",
    "Suvari",
    "Temple",
    "Allen",
    "Silverstone",
    "Walken",
    "West",
    "Keitel",
    "Fawcett",
    "Temple",
    "Hillyer",
    "Stephens",
    "Silva",
    "Santos",
    "Oliveira",
    "Melo",
    "Pereira",
    "Cristo",
    "Prestes",
    "Cunha",
    "Castro",
    "Guerreiro",
    "Lopes",
    "Sousa",
    "Marques",
    "Fernandes",
    "Ribeiro",
    "Zanatta",
    "Zanchete",
    "Pessoto",
    "Albuquerque",
    "Canci",
    "Silveira",
    "Martins",
    "Garcia",
    "Ritter"]

    def geraNome(self):
        '''
        :return: (str) Retorna um nome de uma posição aleatória do vetor de nomes
        '''
        x = random.randint(0, len(self.nomes)-1)
        return self.nomes[x]

    def geraSobrenome(self):
        '''
        :return: (str) Retorna um sobrenome de uma posição aleatória do vetor de sobrenomes
         '''
        x = random.randint(0, len(self.sobrenomes)-1)
        return self.sobrenomes[x]

    def geraIdade(self):
        '''
        :return: (int) Retorna uma idade entre 15 e 100 anos
        '''
        return random.randint(15, 40)

    def geraCodigo(self):
        return random.randint(1000, 9999) 
    
    def geraGols(self):
        return random.randint(0, 100)
    
    def geraPartidas(self):
        return random.randint(0, 100)


