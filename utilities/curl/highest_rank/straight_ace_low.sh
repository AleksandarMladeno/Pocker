curl --location 'http://localhost:8080/api/hand/highest-rank' \
--header 'Content-Type: application/json' \
--data '[
    {
        "value": "A",
        "suit": "S"
    },
    {
        "value": "2",
        "suit": "H"
    },
    {
        "value": "3",
        "suit": "D"
    },
    {
        "value": "4",
        "suit": "C"
    },
    {
        "value": "5",
        "suit": "S"
    }
]'