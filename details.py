
import json

Personal_Info = {
    "basic info":   [
        {
            "Fullname": "Julliane Maeve C. Azuela",
            "Email" : "azi.hulyana@gmail.com",
            "Address" : "General Hizon, Bangkal Makati City",
            "Contact.no" : "+63 939 867 9364"
        }
    ],
    "Education":    [
        {
            "Tertiary" : "Polytechnic University of the Philippines",
            "school1" : "Sta.Mesa, Maynila, Kalakhang Maynila",
            "College" : "College of Engineering",
            "Course" : "Bachelor of Science in Computer Engineering"
        },
        {
            "Secondary" : "Our Lady of Fatima University",
            "school2" : "Lagro, Quezon City",
            "track" : "Science, Technology, Engineering, and Mathematics"
        },
        {
            "Primary" : "Christ's Achievers Montessori",
            "school3" : "Graceville 1, Muzon City of San Jose Del Monte"
        }
    ],
    "Skills":   [
        {
            "Soft Skill1" : "Self-management",
            "Soft Skill2" : "Task-management Skills",
            "Soft Skill3" : "Situational Awareness",
            "Soft Skill4" : "Critical Thinking Skills"
        },
        {
            "Hard Skill1" : "Programming Languages; HTML, Python, C++, PHP",
            "Hard Skill2" : "Knowledgable at MS Office programs; Word, Excel, Access, PowerPoint",
            "Hard Skill3" : "Fluent at 3 languages; Filipino, English, Mandarin"
        }
    ],
    "Experience":  [
        {
            "Profile": "My name is Julliane Maeve, and I finished a Bachelor of Science in Computer Engineering. I am currently a Software Engineer with five (5) years of related experience. I am a proficient worker who's very versatile and works well under pressure. I am also looking forward to working with different projects I have yet to try.",
            "company1" : "Neo Culture Technology",
            "address" : "127 Highway Dream Street, Way V Toronto, Canada",
            "Position" : "Frontend Developer",
            "work" : "Year 2025-2027"
        },
        {
            "company2" : "Foresight Inc.",
            "address" : "Mandaluyong, Metro Manila",
            "position" : "Software Engineer",
            "work" : "2027-2030(current year)"
        }
    ]
}

details = json.dumps(Personal_Info, indent=2)
with open('resume.json', 'w') as f:
    f.write(details)