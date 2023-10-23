curl --location 'http://localhost:8080/api/hand/highest-rank' \
--header 'Content-Type: application/json' \
--data '[
    {
        "value": "2",
        "suit": "C"
    },
    {
        "value": "3",
        "suit": "D"
    },
    {
        "value": "4",
        "suit": "H"
    },
    {
        "value": "5",
        "suit": "D"
    },
    {
        "value": "6",
        "suit": "S"
    }
]'