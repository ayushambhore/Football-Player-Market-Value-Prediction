from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

import json
import time
import csv
import os

URL = "https://sofifa.com/?r=200055&set=true&showCol%5B%5D=pi&showCol%5B%5D=ae&showCol%5B%5D=hi&showCol%5B%5D=wi&showCol%5B%5D=pf&showCol%5B%5D=oa&showCol%5B%5D=pt&showCol%5B%5D=bo&showCol%5B%5D=bp&showCol%5B%5D=gu&showCol%5B%5D=jt&showCol%5B%5D=le&showCol%5B%5D=vl&showCol%5B%5D=wg&showCol%5B%5D=rc&showCol%5B%5D=ta&showCol%5B%5D=cr&showCol%5B%5D=fi&showCol%5B%5D=he&showCol%5B%5D=sh&showCol%5B%5D=vo&showCol%5B%5D=ts&showCol%5B%5D=dr&showCol%5B%5D=cu&showCol%5B%5D=fr&showCol%5B%5D=lo&showCol%5B%5D=bl&showCol%5B%5D=to&showCol%5B%5D=ac&showCol%5B%5D=sp&showCol%5B%5D=ag&showCol%5B%5D=re&showCol%5B%5D=ba&showCol%5B%5D=tp&showCol%5B%5D=so&showCol%5B%5D=ju&showCol%5B%5D=st&showCol%5B%5D=sr&showCol%5B%5D=ln&showCol%5B%5D=te&showCol%5B%5D=ar&showCol%5B%5D=in&showCol%5B%5D=po&showCol%5B%5D=vi&showCol%5B%5D=pe&showCol%5B%5D=cm&showCol%5B%5D=td&showCol%5B%5D=ma&showCol%5B%5D=sa&showCol%5B%5D=sl&showCol%5B%5D=tg&showCol%5B%5D=gd&showCol%5B%5D=gh&showCol%5B%5D=gc&showCol%5B%5D=gp&showCol%5B%5D=gr&showCol%5B%5D=tt&showCol%5B%5D=bs&showCol%5B%5D=wk&showCol%5B%5D=sk&showCol%5B%5D=aw&showCol%5B%5D=dw&showCol%5B%5D=ir&showCol%5B%5D=bt&showCol%5B%5D=hc&showCol%5B%5D=pac&showCol%5B%5D=sho&showCol%5B%5D=pas&showCol%5B%5D=dri&showCol%5B%5D=def&showCol%5B%5D=phy&showCol%5B%5D=t1&showCol%5B%5D=t2&showCol%5B%5D=ps1&showCol%5B%5D=ps2&showCol%5B%5D=tc&showCol%5B%5D=at"
driver = webdriver.Firefox()

driver.get(URL)

time.sleep(1)

count_rows = 0

# Loop through pages
while True:

    football_data = []

    tbody = driver.find_element(By.CSS_SELECTOR, "#body > main:nth-child(2) > article > table > tbody")

    rows = tbody.find_elements(By.TAG_NAME, "tr")

    i = 1
    for row in rows:
        count_rows += 1

        # All tds of each row
        tds = row.find_elements(By.TAG_NAME, "td")
        # print(tds[0].text)

        # photo of player
        image = row.find_element(By.CLASS_NAME, "player-check")

        # Extract image link
        image_link = image.get_attribute("data-srcset")
        # print(image_link.split()[2])

        # Player Name
        Player_Name = tds[1].find_element(By.TAG_NAME, 'a')
        # print(Player_Name.text)

        # Country Name
        country_tag = row.find_element(By.CLASS_NAME, "flag")
        country = country_tag.get_attribute("title")
        # print(f"con : {country}")

        # Country Flag
        country_flag = row.find_element(By.CLASS_NAME, "flag")
        flag_img_link = country_flag.get_attribute("data-srcset")
        # print(flag_img_link.split()[2])

        # position
        position = row.find_element(By.CLASS_NAME, "pos")
        # print(f"pos: {position.text}")

        # age
        age = row.find_element(By.CLASS_NAME, "d2")
        # print(f"age : {age.text}")

        # Overall Rating
        or_td = row.find_element(By.CLASS_NAME, "col-sort")
        overall_rat = or_td.find_element(By.TAG_NAME, "em")
        # print(f"overall rating: {overall_rat.text}")

        # Potential
        potential = row.find_element(By.CSS_SELECTOR,
                                     f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(5) > em")
        # print(f"potential : {potential.text}")

        # Team logo
        try:
            team_img_tag = row.find_element(By.CLASS_NAME, "team")
            team_logo = team_img_tag.get_attribute("data-srcset")
        except NoSuchElementException:
            team_img_tag = tds[5].find_element(By.CLASS_NAME, "flag")
            team_logo = country_flag.get_attribute("data-srcset")
        # print(team_logo.split()[2])

        # Team Name
        team_name = row.find_element(By.CSS_SELECTOR,
                                     f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(6) > a")
        # print(f"Team Name: {team_name.text}")

        # Contract
        contract = row.find_element(By.CSS_SELECTOR,
                                    f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(6) > div")
        # print(f"Contract: {contract.text}")

        # ID
        id_ = row.find_element(By.CSS_SELECTOR,
                               f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(7)")
        # print(f"ID: {id_.text}")

        # Height
        height = row.find_element(By.CSS_SELECTOR,
                                  f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(8)")
        # print(f"height: {height.text}")

        # Weight
        weight = row.find_element(By.CSS_SELECTOR,
                                  f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(9)")
        # print(f"weight: {weight.text}")

        # foot
        foot = row.find_element(By.CSS_SELECTOR,
                                f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(10)")
        # print(f"foot : {foot.text}")

        # Best overall
        best_overall = row.find_element(By.CSS_SELECTOR,
                                        f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(11) > em")
        # print(f"Best overall: {best_overall.text}")

        # Best Position
        best_pos = row.find_element(By.CSS_SELECTOR,
                                    f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(12) > a > span")
        # print(f"best pos : {best_pos.text}")
        # Growth
        growth = row.find_element(By.CSS_SELECTOR,
                                  f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(13) > em")
        # print(f"growth : {growth.text}")

        # joined date
        joined_date = row.find_element(By.CSS_SELECTOR,
                                       f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(14)")
        # print(f"joined date : {joined_date.text}")

        # Loan Date end
        loan_date_end = row.find_element(By.CSS_SELECTOR,
                                         f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(15)")
        # print(f"Loan Date end: {loan_date_end.text}")

        # Value
        value = row.find_element(By.CSS_SELECTOR,
                                 f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(16)")
        # print(f"Value: {value.text}")

        # Wage
        wage = row.find_element(By.CSS_SELECTOR,
                                f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(17)")
        # print(f"wage: {wage.text}")

        # Release clause
        rel_clause = row.find_element(By.CSS_SELECTOR,
                                      f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(18)")
        # print(f"Release clause: {rel_clause.text}")

        # total Attacking
        total_att = row.find_element(By.CSS_SELECTOR,
                                     f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(19) > em")
        # print(f"total Attacking: {total_att.text}")

        # Crossing
        crossing = row.find_element(By.CSS_SELECTOR,
                                    f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(20) > em")
        # print(f"crossing: {crossing.text}")

        # Finishind
        finishing = row.find_element(By.CSS_SELECTOR,
                                     f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(21) > em")
        # print(f"finishing : {finishing.text}")

        # Heading accuracy
        Head_acc = row.find_element(By.CSS_SELECTOR,
                                    f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(22) > em")

        # Short Passing
        short_pass = row.find_element(By.CSS_SELECTOR,
                                      f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(23) > em")

        # Volleys
        volleys = row.find_element(By.CSS_SELECTOR,
                                   f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(24) > em")

        # Total Skill
        total_skill = row.find_element(By.CSS_SELECTOR,
                                       f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(25) > em")

        # Dribbling
        dribbling = row.find_element(By.CSS_SELECTOR,
                                     f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(26) > em")

        # curve
        curve = row.find_element(By.CSS_SELECTOR,
                                 f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(27) > em")

        # Fk Accuracy
        fk_acc = row.find_element(By.CSS_SELECTOR,
                                  f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(28) > em")

        # Long Passing
        long_pass = row.find_element(By.CSS_SELECTOR,
                                     f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(29) > em")

        # Ball control
        ball_control = row.find_element(By.CSS_SELECTOR,
                                        f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(30) > em")

        # Total Movement
        total_mov = row.find_element(By.CSS_SELECTOR,
                                     f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(31) > em")

        # Acceleration
        Acceleration = row.find_element(By.CSS_SELECTOR,
                                        f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(32) > em")

        # Sprint speed
        Sprint_speed = row.find_element(By.CSS_SELECTOR,
                                        f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(33) > em")

        # Agility
        agility = row.find_element(By.CSS_SELECTOR,
                                   f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(34) > em")

        # Reactions
        reaction = row.find_element(By.CSS_SELECTOR,
                                    f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(35) > em")

        # Balance
        bal = row.find_element(By.CSS_SELECTOR,
                               f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(36) > em")

        # Total Power
        total_pow = row.find_element(By.CSS_SELECTOR,
                                     f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(37) > em")

        # Shot Power
        shot_pow = row.find_element(By.CSS_SELECTOR,
                                    f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(38) > em")

        # jumping
        jump = row.find_element(By.CSS_SELECTOR,
                                f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(39) > em")

        # Stamina
        stamina = row.find_element(By.CSS_SELECTOR,
                                   f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(40) > em")

        # Strength
        strength = row.find_element(By.CSS_SELECTOR,
                                    f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(41) > em")

        # Long shots
        long_stots = row.find_element(By.CSS_SELECTOR,
                                      f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(42) > em")

        # Total mentality
        total_mentality = row.find_element(By.CSS_SELECTOR,
                                           f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(43) > em")

        # Aggression
        aggresion = row.find_element(By.CSS_SELECTOR,
                                     f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(44) > em")

        # Interceptions
        interception = row.find_element(By.CSS_SELECTOR,
                                        f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(45) > em")

        # Att. position
        att_pos = row.find_element(By.CSS_SELECTOR,
                                   f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(46) > em")

        # vision
        vision = row.find_element(By.CSS_SELECTOR,
                                  f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(47) > em")

        # penalties
        penalties = row.find_element(By.CSS_SELECTOR,
                                     f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(48) > em")

        # Composure
        composure = row.find_element(By.CSS_SELECTOR,
                                     f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(49) > em")

        # Total Defending
        Tl_defending = row.find_element(By.CSS_SELECTOR,
                                        f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(50) > em")

        # Defensive Awareness
        def_awareness = row.find_element(By.CSS_SELECTOR,
                                         f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(51) > em")

        # Standing tackle
        stack_tackle = row.find_element(By.CSS_SELECTOR,
                                        f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(52) > em")

        # sliding tackle
        sliding_tackle = row.find_element(By.CSS_SELECTOR,
                                          f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(53) > em")

        # total Goalkeeping
        tl_goalkeeping = row.find_element(By.CSS_SELECTOR,
                                          f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(54) > em")

        # Gk Diving
        gk_diving = row.find_element(By.CSS_SELECTOR,
                                     f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(55) > em")

        #  GK Handling
        gk_handling = row.find_element(By.CSS_SELECTOR,
                                       f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(56) > em")

        # GK kicking
        gk_kicking = row.find_element(By.CSS_SELECTOR,
                                      f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(57) > em")

        # gk positioning
        gk_pos = row.find_element(By.CSS_SELECTOR,
                                  f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(58) > em")

        # GK Reflexes
        gk_reflexes = row.find_element(By.CSS_SELECTOR,
                                       f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(59) > em")

        # Total stats
        total_stats = row.find_element(By.CSS_SELECTOR,
                                       f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td.d5 > em")
        # print(f"Total stats: {total_stats.text}")

        # Base stats
        base_stat = row.find_element(By.CSS_SELECTOR,
                                     f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(61) > em")

        # Week foot
        week_foot = row.find_element(By.CSS_SELECTOR,
                                     f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(62)")
        # print(f"week_foot: {week_foot.text}")

        # Skill moves
        skill_mov = row.find_element(By.CSS_SELECTOR,
                                     f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(63)")
        # print(f"skill moves: {skill_mov.text}")

        # attacking work rate
        att_work_rate = row.find_element(By.CSS_SELECTOR,
                                         f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(64)")

        # Defensive work rate
        def_work_rate = row.find_element(By.CSS_SELECTOR,
                                         f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(65)")

        # International reputation
        internation_repu = row.find_element(By.CSS_SELECTOR,
                                            f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(66)")

        # Body type
        body_type = row.find_element(By.CSS_SELECTOR,
                                     f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(67)")

        # Real Face
        real_face = row.find_element(By.CSS_SELECTOR,
                                     f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(68)")

        # Pace / Diving
        pace_diving = row.find_element(By.CSS_SELECTOR,
                                       f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(69) > em")

        # Shooting / Handling
        shoot_handling = row.find_element(By.CSS_SELECTOR,
                                          f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(70) > em")

        # Passing / kicking
        passing_kicking = row.find_element(By.CSS_SELECTOR,
                                           f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(71) > em")

        # Dribbling/Reflexes
        dr = row.find_element(By.CSS_SELECTOR,
                              f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(72) > em")
        # print(f"DR: {dr.text}")

        # Defending/pace
        dp = row.find_element(By.CSS_SELECTOR,
                              f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(73) > em")
        # print(f"dp: {dp.text}")

        # Physical / Positioning
        physical_pos = row.find_element(By.CSS_SELECTOR,
                                        f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(74) > em")
        # print(f"physical Positioning: {physical_pos.text}")

        # Traits 1
        traits_1 = row.find_element(By.CSS_SELECTOR,
                                    f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(75)")

        # Traits 2
        traits_2 = row.find_element(By.CSS_SELECTOR,
                                    f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(76)")

        # PlayStyles
        play_styles_td = row.find_element(By.CSS_SELECTOR,
                                          f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(77)")
        play_styles_spans = play_styles_td.find_elements(By.TAG_NAME, "span")
        play_styles = []
        for ps in play_styles_spans:
            play_styles.append(ps.text)

        # PlayStyles+
        try:
            play_styles_plus = row.find_element(By.CSS_SELECTOR,
                                                f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(78) > span")
        except NoSuchElementException:
            play_styles_plus = row.find_element(By.CSS_SELECTOR,
                                                f"body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(78)")

        # No. of playStyles
        no_of_play_st = row.find_element(By.CSS_SELECTOR,
                                         f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(79) > em")

        # Acceleration Type
        acc_type = row.find_element(By.CSS_SELECTOR,
                                    f"#body > main:nth-child(2) > article > table > tbody > tr:nth-child({i}) > td:nth-child(80)")

        item = {
            "Player Img Link": image_link.split()[2],
            "Name": f"{Player_Name.text}",
            "Country": country,
            "Country Flag": flag_img_link.split()[2],
            "Position": position.text,
            "Age": age.text,
            "Overall rating": overall_rat.text,
            "Potential": potential.text,
            "Team Logo": team_logo.split()[2],
            "Team Name": team_name.text,
            "Contract": contract.text,
            "ID": id_.text,
            "Height": height.text,
            "Weight": weight.text,
            "foot": foot.text,
            "Best overall": best_overall.text,
            "Best position": best_pos.text,
            "Growth": growth.text,
            "Joined Date": joined_date.text,
            "Loan date end": loan_date_end.text,
            "Value": value.text,
            "Wage": wage.text,
            "Release clause": rel_clause.text,
            "Total attacking": total_att.text,
            "Crossing": crossing.text,
            "Finishing": finishing.text,
            "Heading accuracy": Head_acc.text,
            "Short passing": short_pass.text,
            "Volleys": volleys.text,
            "Total skill": total_skill.text,
            "Dribbling": dribbling.text,
            "Curve": curve.text,
            "FK Accuracy": fk_acc.text,
            "Long passing": long_pass.text,
            "Ball control": ball_control.text,
            "Total movement": total_mov.text,
            "Acceleration": Acceleration.text,
            "Sprint speed": Sprint_speed.text,
            "Agility": agility.text,
            "Reactions": reaction.text,
            "Balance": bal.text,
            "Total power": total_pow.text,
            "Shot power": shot_pow.text,
            "Jumping": jump.text,
            "Stamina": stamina.text,
            "Strength": strength.text,
            "Long shots": long_stots.text,
            "Total mentality": total_mentality.text,
            "Aggression": aggresion.text,
            "Interceptions": interception.text,
            "Att. Position": att_pos.text,
            "Vision": vision.text,
            "Penalties": penalties.text,
            "Composure": composure.text,
            "Total defending": Tl_defending.text,
            "Defensive awareness": def_awareness.text,
            "Standing tackle": stack_tackle.text,
            "Sliding tackle": sliding_tackle.text,
            "Total goalkeeping": tl_goalkeeping.text,
            "GK Diving": gk_diving.text,
            "GK Handling": gk_handling.text,
            "GK Kicking": gk_kicking.text,
            "GK Positioning": gk_pos.text,
            "GK Reflexes": gk_reflexes.text,
            "Total Stats": total_stats.text,
            "Base stats": base_stat.text,
            "Weak foot": week_foot.text,
            "Skill moves": skill_mov.text,
            "Attacking work rate": att_work_rate.text,
            "Defensive work rate": def_work_rate.text,
            "International reputation": internation_repu.text,
            "Body type": body_type.text,
            "Real face": real_face.text,
            "Pace / Diving": pace_diving.text,
            "Shooting / Handling": shoot_handling.text,
            "Passing / Kicking": passing_kicking.text,
            "Dribbling / Reflexes": dr.text,
            "Defending / pace": dp.text,
            "Physical / Positioning": physical_pos.text,
            "Traits_1": traits_1.text,
            "Traits_2": traits_2.text,
            "PlayStyles": play_styles,
            "PlayStyles +": play_styles_plus.text,
            "Number of playstyles": no_of_play_st.text,
            "Acceleration Type": acc_type.text
        }


        i += 1

        football_data.append(item)

    filename = 'FIFA_20_aug_6_2020.csv'
    fieldnames = [
        "Player Img Link", "Name", "Country", "Country Flag", "Position", "Age", "Overall rating",
        "Potential", "Team Logo", "Team Name", "Contract", "ID", "Height", "Weight", "foot", "Best overall",
        "Best position", "Growth", "Joined Date", "Loan date end", "Value", "Wage", "Release clause",
        "Total attacking", "Crossing", "Finishing", "Heading accuracy", "Short passing",
        "Volleys", "Total skill", "Dribbling", "Curve", "FK Accuracy", "Long passing",
        "Ball control", "Total movement", "Acceleration", "Sprint speed", "Agility",
        "Reactions", "Balance", "Total power", "Shot power", "Jumping", "Stamina",
        "Strength", "Long shots", "Total mentality", "Aggression", "Interceptions",
        "Att. Position", "Vision", "Penalties", "Composure", "Total defending",
        "Defensive awareness", "Standing tackle", "Sliding tackle", "Total goalkeeping",
        "GK Diving", "GK Handling", "GK Kicking", "GK Positioning", "GK Reflexes", "Total Stats",
        "Base stats", "Weak foot", "Skill moves", "Attacking work rate",
        "Defensive work rate", "International reputation", "Body type", "Real face",
        "Pace / Diving", "Shooting / Handling", "Passing / Kicking", "Dribbling / Reflexes", "Defending / pace",
        "Physical / Positioning", "Traits_1", "Traits_2", "PlayStyles", "PlayStyles +", "Number of playstyles",
        "Acceleration Type"
    ]

    # Write data to CSV
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        file_is_empty = not os.path.exists(filename) or os.stat(filename).st_size == 0
        if file_is_empty:
            writer.writeheader()
        for item in football_data:
            writer.writerow(item)

    print(f"Number of Rows covered: {count_rows}")
    time.sleep(1)
    try:
        print("NEXT page")
        Next_button = driver.find_element(By.LINK_TEXT, "Next")

        # Scroll into view
        driver.execute_script("arguments[0].scrollIntoView();", Next_button)
        time.sleep(5)

        Next_button.click()

    except NoSuchElementException:
        print("End of pages")
        break

print(f"Data successfully saved to {filename}")

driver.close()