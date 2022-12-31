from PIL import Image, ImageDraw, ImageFont
from datetime import date, timedelta


def gregorian_to_jalali(gy, gm, gd):
    g_d_m = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    if gm > 2:
        gy2 = gy + 1
    else:
        gy2 = gy
    days = (355666 + (365 * gy) + ((gy2 + 3) // 4) - ((gy2 + 99) // 100) +
            ((gy2 + 399) // 400) + gd + g_d_m[gm - 1])
    jy = -1595 + (33 * (days // 12053))
    days %= 12053
    jy += 4 * (days // 1461)
    days %= 1461
    if days > 365:
        jy += (days - 1) // 365
        days = (days - 1) % 365
    if days < 186:
        jm = 1 + (days // 31)
        jd = 1 + (days % 31)
    else:
        jm = 7 + ((days - 186) // 30)
        jd = 1 + ((days - 186) % 30)
    return [jy, jm, jd]


def m_convert(month):
    switch = {
        1: "فروردین",
        2: "اردیبهشت",
        3: "خرداد",
        4: "تیر",
        5: "مرداد",
        6: "شهریور",
        7: "مهر",
        8: "آبان",
        9: "آذر",
        10: "دی",
        11: "بهمن",
        12: "اسفند",
    }
    return switch.get(month)


def get_week_day(day):
    weekdays = {
        0: ["Saturday", "شنبه"],
        1: ["Sunday", "یکشنبه"],
        2: ["Monday", "دوشنبه"],
        3: ["Tuesday", "سه شنبه"],
        4: ["Wednesday", "چهارشنبه"],
        5: ["Thursday", "پنجشنبه"],
    }
    return weekdays.get(day)


def get_date():
    week_day = date.weekday(date.today()) + 2
    today = date.today()
    current = today-timedelta(days=week_day)
    if week_day == 7:
        current += timedelta(days=7)
    e_date = []
    p_date = []
    for i in range(0, 6):
        day = current.strftime("%d")
        num_month = current.strftime("%m")
        month = current.strftime("%B")
        year = current.strftime("%Y")
        j_year, j_month, j_day = gregorian_to_jalali(
            int(year), int(num_month), int(day))
        current += timedelta(days=1)
        e_date.append([str(year), str(month), str(day)])
        p_date.append([str(j_year), str(j_day), str(m_convert(j_month))])
        # e_date: [['2022','May','12'],...]
        # p_date: [['1401','2','دی'],...]
        print(e_date[i])
        print(p_date[i])
    return e_date, p_date


def form(e_date, p_date):
    month = e_date[1]
    day = e_date[2]
    year = e_date[0]

    j_day, j_month, j_year = p_date[1], p_date[2], p_date[0]

    img = Image.open("./Price Table-template.png")
    d = ImageDraw.Draw(img)
    p_font = ImageFont.truetype("./B Titr Bold.ttf", 110)
    e_font = ImageFont.truetype("./Myriad Pro Bold.ttf", 100)

    # persian date
    # year
    d.text((390, 350), j_year, fill=(0, 0, 0), font=p_font)
    # month
    d.text(
        (820, 400),
        j_month,
        fill=(0, 0, 0),
        anchor="mm",
        font=p_font,
    )
    # day
    d.text((1060, 350), j_day, fill=(0, 0, 0), font=p_font)

    # english date
    # day
    d.text(
        (350, 480),
        day,
        fill=(0, 0, 0),
        font=e_font,
    )
    # month
    d.text(
        (730, 530),
        month,
        anchor="mm",
        fill=(0, 0, 0),
        font=e_font,
    )
    # year
    d.text(
        (1000, 480),
        year,
        fill=(0, 0, 0),
        font=e_font,
    )
    img.save("./Price Table.png")


def calender(e_date, p_date):
    p_font = ImageFont.truetype("./B Titr Bold.ttf", 110)
    e_font = ImageFont.truetype("./Myriad Pro Bold.ttf", 100)
    for i in range(0, 6):
        img = Image.open("./Date-template.jpg")
        d = ImageDraw.Draw(img)

        day = e_date[i][0]
        month = e_date[i][1]
        year = e_date[i][2]

        j_day = p_date[i][0]
        j_month = p_date[i][1]
        j_year = p_date[i][2]

        weekday = get_week_day(i)
        
        
        
        


def main():
    e_date, p_date = get_date()
    form(e_date[0], p_date[0])


if __name__ == "__main__":
    main()