from django.shortcuts import render


def index(request):
    nav_link = [
        {"link": "/#home", "name": "Home"},
        {"link": "/#about", "name": "About"},
        {"link": "/#projects", "name": "Projects"},
        {"link": "/#skills", "name": "Skills"},
        {"link": "/#experience", "name": "Experience"},
        {"link": "/#gallery", "name": "Gallery"},
        {"link": "/#contact", "name": "Contact"},
    ]

    about = [
        "Hai! Nama saya Kaloka Radia Nanda, dan saya siswa SMP kelas 1. Saya punya hobi yang mungkin sedikit berbeda dari teman-teman lain, yaitu coding. Sejak pertama kali kenal komputer, saya langsung suka banget sama dunia pemrograman. Menulis kode dan melihatnya bekerja itu rasanya seru banget!",
        "Saya suka menghabiskan waktu luang dengan belajar bahasa pemrograman baru dan membuat proyek-proyek kecil yang keren. Mulai dari bikin game sederhana, aplikasi kecil, sampai coba-coba bikin situs web. Buat saya, coding bukan cuma hobi, tapi juga cara untuk berkreativitas dan bersenang-senang.",
        "Lewat website ini, saya ingin berbagi cerita tentang perjalanan saya di dunia coding dan proyek-proyek yang sudah saya buat. Semoga bisa menginspirasi teman-teman untuk mencoba hal baru dan mengejar apa yang mereka sukai. Terima kasih sudah berkunjung, semoga suka!",
    ]

    projects = [
        {
            "name": "Flamingoo Note",
            "description": "Aplikasi catatan online sederhana yang saya buat dengan React dan Vite.",
            "link": "https://flamingoo-note.vercel.app/",
        },
        {
            "name": "Tic Tac Toe With React",
            "description": "Permainan tic tac toe online sederhana yang saya buat dengan React dan Vite.",
            "link": "https://ttt-with-react.vercel.app/",
        },
        {
            "name": "My Portfolio (Next.js)",
            "description": "Website portfolio pribadi saya yang saya buat dengan React dan Next.js serta TailwindCSS juga template dari Flowbite.",
            "link": "https://kalokaradiananda.my.id/",
        },
        {
            "name": "I Love Anime List",
            "description": "Aplikasi list anime online sederhana yang saya buat dengan Next.js dan React serta Jikan API.",
            "link": "https://github.com/kalokaradia/I-Love-Anime-List",
        },
        {
            "name": "Flamingoo Note",
            "description": "Aplikasi catatan online sederhana yang saya buat dengan React dan Vite.",
            "link": "https://flamingoo-note.vercel.app/",
        },
        {
            "name": "Oka CSS",
            "description": "Framework CSS sederhana yang saya buat dengan SASS dan saya publish ke NPM.",
            "link": "https://github.com/kalokaradia/OkaCSS",
        },
        {
            "name": "Science Finder",
            "description": "Aplikasi pencari kosakata sains yang saya buat dengan Next.js dan React serta science-finder API yang saya buat sendiri.",
            "link": "http://science-finder.vercel.app/",
        },
        {
            "name": "science-finder API",
            "description": "API kosakata sains buatan saya.",
            "link": "https://science-api.vercel.app/vocability.json",
        },
        {
            "name": "Star Band SMP N 1 Purworejo",
            "description": "Website Band SMP N 1 Purworejo yaitu Star Band yang saya buat dengan Next.js dan React.",
            "link": "https://github.com/kalokaradia/OkaCSS",
        },
        {
            "name": "OSISPENSA",
            "description": "Website OSIS SMP N 1 Purworejo yang saya buat dengan Next.js dan React serta menggunakan template Edumon.",
            "link": "https://osispensa.vercel.app",
        },
        {
            "name": "Temperature Converter",
            "description": "Aplikasi konversi suhu sederhana yang saya buat dengan Django dan Bootstrap 5.",
            "link": "https://github.com/kalokaradia/temperature-converter",
        },
        {
            "name": "My Portfolio (Django)",
            "description": "Website portfolio pribadi saya yang saya buat dengan Django dan TailwindCSS serta template dari Flowbite.",
            "link": "/",
        },
    ]

    skills = [
        "HTML",
        "CSS",
        "JavaScript",
        "TypeScript",
        "Node.js",
        "React",
        "Next.js",
        "Vite",
        "TailwindCSS",
        "Bootstrap",
        "PHP",
        "Laravel",
        "SASS",
        "C++",
        "Pascal",
        "Python",
        "Django",
    ]

    achievements = [
        {
            "event": "NEW INTERMEDIATE 1 Kategori Sempi",
            "date": "2019-01-13",
            "description": "Saya mengikuti kejuaraan SEMPOA SIP se-Jawa Tengah dan mendapat juara harapan 2.",
        },
        {
            "event": "Ar-Rois Language and Science Olympiad (ALSO)",
            "date": "2023-04-03",
            "description": "Saya mengikuti olimpiade ALSO pada tanggal 3 bulan April tahun 2023 di bidang bahasa Inggris.",
        },
        {
            "event": "ISC Se Jawa Tengah 2023",
            "date": "2023-06-12",
            "description": "Saya mengikuti olimpiade ISC Se Jawa Tengah 2023 di bidang Matematika terintegrasi.",
        },
        {
            "event": "IISC 2023",
            "date": "2023-08-20",
            "description": "Saya mengikuti olimpiade IISC 2023 di bidang Matematika terintegrasi.",
        },
        {
            "event": "MSC 2023",
            "date": "2023-08-20",
            "description": "Saya mengikuti olimpiade MSC 2023 di bidang Matematika.",
        },
        {
            "event": "FUSO 2023",
            "date": "2023-09-24",
            "description": "Saya mengikuti olimpiade FUSO 2023 di bidang Matematika.",
        },
        {
            "event": "BIG BANG COMPETITION 2",
            "date": "2023-10-07",
            "description": "Saya mengikuti olimpiade BIG BANG COMPETITION 2 di bidang Matematika.",
        },
        {
            "event": "PIMO 2023",
            "date": "2023-10-29",
            "description": "Saya mengikuti olimpiade PIMO 2023 di bidang Matematika.",
        },
        {
            "event": "Olimpiade Sains dan Agama (OSMA)",
            "date": "2024-02-28",
            "description": "Saya mengikuti olimpiade OSMA di bidang Matematika, IPA, dan TIK.",
        },
        {
            "event": "Olimpiade PAI Nasional (OPIN)",
            "date": "2024-03-31",
            "description": "Saya mengikuti olimpiade OSMA di bidang PAI.",
        },
        {
            "event": "Peringkat 2 Asesmen Madrasah",
            "date": "2024-06-11",
            "description": "Saya mendapat peringkat ke-2 dalam Asesmen Madrasah TP. 2023/2024.",
        },
        {
            "event": "EMC (Eduversal Mathematics Competition)",
            "date": "2024-11-16",
            "description": "Saya mengikuti salah satu kompetisi matematika tingkat nasional yaitu EMC.",
        },
    ]

    img_gallery = ["/img/jumbotron.jpg"]

    return render(
        request,
        "index.html",
        {
            "nav_link": nav_link,
            "about": about,
            "projects": projects,
            "skills": skills,
            "achievements": achievements,
            "gallery": img_gallery,
        },
    )
