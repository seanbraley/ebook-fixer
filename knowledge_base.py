__author__ = 'sean.braley'

exclusion_words = (
    'Whose', 'What', "ever'", 'Whosever', 'thees', 'its', 'whose', 'His', 'enny', 'anye',
    'Both', 'them', 'his', 'whichever', 'every', 'thet', 'ther', 'Whatever', 'these',
    'hys', 'either', 'each', "another's", 'some', 'Which', 'our', 'Neither', 'out',
    'what', 'thease', 'That', 'your', "Y'r", 'neither', 'This', 'Either', 'Each',
    'yore', 'My', 'both', 'whichever-the-hell', 'Your', 'thine', 'Her', 'No', 'whatever',
    'one', 'Their', 'another', "'nother", 'ether', 'her', 'their', 'Whichever', 'Every',
    'Those', 'that', 'These', 'ani', 'those', 'hir', 'this', 'nether', 'Our', 'my',
    'Any', 'mine', 'an', 'myn', 'any', 'Them', 'no', 'Ye', 'which', "th'", 'A', 'Thy',
    'mah', 'The', 'myne', 'a', 'thy', 'Some', 'An', 'Another', 'the', 'Its', 'I'
)

authors_pulp = {
    'high': [
        'Poul Anderson',
        'Isaac Asimov',
        'Charles Beadle',
        'H. Bedford-Jones',
        'Robert Leslie Bellem',
        'Alfred Bester',
        'Robert Bloch',
        'B. M. Bower',
        'Leigh Brackett',
        'Ray Bradbury',
        'Max Brand',
        'Fredric Brown',
        'Edgar Rice Burroughs',
        'William S. Burroughs',
        'Ellis Parker Butler',
        'Hugh B. Cave',
        'Paul Chadwick',
        'Raymond Chandler',
        'Agatha Christie',
        'Arthur C. Clarke',
        'Joseph Conrad',
        'Stephen Crane',
        'Ray Cummings',
        'Jason Dark',
        'Lester Dent',
        'August Derleth',
        'Philip K. Dick',
        'Arthur Conan Doyle',
        'J. Allan Dunn',
        'Lord Dunsany',
        'C. M. Eddy, Jr.',
        'Arthur Guy Empey',
        'George Allan England',
        'C. S. Forester',
        'F. Scott Fitzgerald',
        'Arthur O. Friel',
        'Erle Stanley Gardner',
        'Walter B. Gibson',
        'David Goodis',
        'L. Patrick Greene',
        'Zane Grey',
        'Frank Gruber',
        'H. Rider Haggard',
        'Edmond Hamilton',
        'Dashiell Hammett',
        'Margie Harris',
        'Robert A. Heinlein',
        'O. Henry',
        'Frank Herbert',
        'Robert E. Howard',
        'L. Ron Hubbard',
        'Carl Jacobi',
        'Ardyth Kennelly',
        'Donald Keyhoe',
        'Rudyard Kipling',
        'Henry Kuttner',
        'Harold Lamb',
        'Louis L\'Amour',
        'Margery Lawrence',
        'Fritz Leiber',
        'Murray Leinster',
        'Elmore John Leonard',
        'Jack London',
        'H. P. Lovecraft',
        'Giles A. Lutz',
        'John D. MacDonald',
        'Elmer Brown Mason',
        'F. Van Wyck Mason',
        'Horace McCoy',
        'Johnston McCulley',
        'William Colt MacDonald',
        'Merriam Modell',
        'C.L. Moore',
        'Walt Morey',
        'Talbot Mundy',
        'Philip Francis Nowlan',
        'Fulton Oursler',
        'Hugh Pendexter',
        'Emil Petaja',
        'E. Hoffmann Price',
        'Seabury Quinn',
        'John H. Reese',
        'Tod Robbins',
        'Sax Rohmer',
        'Theodore Roscoe',
        'Rafael Sabatini',
        'Charles Alden Seltzer',
        'Stephen Shadegg',
        'Richard S. Shaver',
        'Robert Silverberg',
        'Bertrand William Sinclair',
        'Upton Sinclair',
        'Arthur D. Howden Smith',
        'Clark Ashton Smith',
        'E. E. Smith',
        'T.S. Stribling',
        'Jim Thompson',
        'Thomas Thursday',
        'W.C. Tuttle',
        'Mark Twain',
        'Jack Vance',
        'E. C. Vivian',
        'H. G. Wells',
        'Henry S. Whitehead',
        'Raoul Whitfield',
        'Tennessee Williams',
        'Cornell Woolrich',
        'Gordon Young',
        # Clark austin smith
    ],
    # Based on 'Similar to Charles Dickens'
    'low':
    [
        'Charles Dickens',
        'George Eliot',
        'Wilkie Collins',
        'George Grossmith',
        'Hans Christian Andersen',
        'Anthony Trollope',
        'Henry Fielding',
        'Joseph Conrad',
        'Henry James',
        'Alexandre Dumas',
        'Gustave Flaubert',
        'Walter Scott',
        'Geoffrey Chaucer',
        'O. Henry',
        'Robert Tressell',
        'Thomas Hardy',
        'Henry van Dyke',
        'E.M. Forster',
        'Elizabeth Gaskell',
        'R.D. Blackmore',
        'George Gissing',
    ]
}

genres_pulp = {
    'high':
    [
        'Adventure',
        'Aviation',
        'Detective',
        'Mystery',
        'Fantasy',
        'Gangster',
        'Horror',
        'Occult',
        'Humor',
        'Railroad',
        'Romance',
        'Science Fiction',
        'Sports',
        'War',
        'Westerns',
    ],
    'low':
    [
        
    ]
}

transition_words = {
    'adverbs':
    (
        'Accordingly',
        'Also',
        'Anyway ',
        'Besides',
        'Certainly',
        'Consequently',
        'Finally',
        'Furthermore',
        'Hence',
        'However',
        'Incidentally',
        'Indeed',
        'Instead',
        'Likewise',
        'Meanwhile',
        'Moreover',
        'Nevertheless',
        'Next',
        'Nonetheless',
        'Now',
        'Otherwise',
        'Similarly',
        'Stil',
        'then',
        'Thereafter',
        'Therefore',
        'Thus',
        'Undoubtedly',
        # Added SBraley March 29th


    ),
    'phrases':
    (
        'In addition',
        'In contrast',
        'For example',
        'For instance',
        'Of course',
        'As a result',
        'In other words',
    ),
    'implied':
    (
        'These',
    ),
    'custom':
    (
        'During',
        'Even',
        'Then',
        'In',
        'Of',
        'As',

    )
}