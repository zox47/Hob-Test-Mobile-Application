from flet import *
import requests


def main(page: Page):
    contacts = []
    page.window_height = 780
    page.window_width = 420
    page.theme_mode = "DARK"
    profile = ""
    #page.theme_mode = ThemeMode.LIGHT
    #page.update()

    contactlist = Ref[ListView(expand=1, divider_thickness=1, spacing=10, padding=0, auto_scroll=False)]()
    progress = ProgressRing(width=20, height=20, stroke_width=2,)
    telephonefix = TextField(border_color=colors.WHITE70, prefix_icon=icons.CALL, )
    telephonemobile = TextField(border_color=colors.WHITE70, prefix_icon=icons.CALL, )
    nomsok = TextField(border_color=colors.WHITE70)
    prenomok = TextField(border_color=colors.WHITE70)
    emailsok = TextField(border_color=colors.WHITE70, prefix_icon=icons.EMAIL, icon=Switch(width=54, value=True),)
    nameprofile = Text("", size=20, color=colors.WHITE)
    logo = Text("Hope Oline",color=colors.WHITE70)
    emm = Text(value="HHHH",color=colors.WHITE70)
    nuum = Text(value="+212693039405",color=colors.WHITE70)
    sessionname = Text("Bonjour Abdo",size=20)
    logox = Text("Hope Oline", size=10)

    def back(e):
        page.go("/MENU")

    pic = Container(padding=10, content=Row(alignment=alignment.center,controls=[
        Stack([
            CircleAvatar(
                foreground_image_url="https://avatars.githubusercontent.com/u/5041459?s=88&v=4"
            ),

        ]),

    ]))



    async def button_click(e):
        page.controls.append(Text("Hello!"))
        await page.update_async()
    import json
    sessionxx = requests.get("https://api-v2.hopcrm.com/api/mobile/sessions/infos").content
    json_data = json.loads(sessionxx)

    # Extract the desired fields


    nomss = json_data['user']['nom']
    prenomss = json_data['user']['prenom']
    logoss = json_data['client']['nom']

    sessionname.value = f"{prenomss} {nomss}"
    logox.value = logoss


    org = requests.get("https://api-v2.hopcrm.com/api/mobile/infos/volumetrie").content

    json_datas = json.loads(org)
    con = json_datas['contact']
    act = json_datas['action']
    lig = json_datas['ligne']
    nots = json_datas['note']
    pice = json_datas['piece']
    orga = json_datas['organisation']
    affa = json_datas['affaire']
    prod = json_datas['produit']


    contactvalue = Text(
                                value=con,
                                size=20,
                                weight=FontWeight.BOLD,
                                color="WHITE",

                            )


    dashboardvalue = Text(
                                value=lig,
                                size=20,
                                weight=FontWeight.BOLD,
                                color="WHITE",

                            )
    notesvalue =  Text(
                                value=nots,
                                size=20,
                                weight=FontWeight.BOLD,
                                color="WHITE",

                            )
    piecesvalue = Text(
                                value=pice,
                                size=20,
                                weight=FontWeight.BOLD,
                                color="WHITE",

                            )
    tachesvalue = Text(
                                value=act,
                                size=20,
                                weight=FontWeight.BOLD,
                                color="WHITE",

                            )
    entreprisevalue = Text(
                                value=orga,
                                size=20,
                                weight=FontWeight.BOLD,
                                color="WHITE",

                            )
    affairesvalue = Text(
                                value=affa,
                                size=20,
                                weight=FontWeight.BOLD,
                                color="WHITE",

                            )
    produitvalue = Text(
                                value=prod,
                                size=20,
                                weight=FontWeight.BOLD,
                                color="WHITE",

                            )

    def route_change(route):
        page.views.clear()
        page.views.append(
            View(
                "/MENU",
        [

            AppBar(

                color="white",
                leading=pic,
                leading_width=40,
                title=ListTile(width=300,
                            title=sessionname,
                            subtitle=logox),

                center_title=False,
                bgcolor=colors.SURFACE_VARIANT,
                actions=[
                    IconButton(icons.NOTIFICATIONS_ROUNDED),
                    IconButton(icons.MENU),

                ],
            ),

            Column(alignment=alignment.center,controls=[

                Row(alignment=MainAxisAlignment.CENTER, controls=[
                    Container(
                        on_click=ok,
                        padding=(12),
                        margin=(15),
                        width=160,
                        height=130,
                        bgcolor=colors.GREY,
                        border_radius=10,
                        animate_opacity=300,

                        content=Column(spacing=35,controls=[
                            Row(alignment=MainAxisAlignment.END,controls=[
                                contactvalue,



                            ]),
                            Text(
                                value="Contacts",
                                size=20,
                                weight=FontWeight.BOLD,
                                color="WHITE",

                            ),

                        ],),

                    ),
                    Container(
                        on_click=ok,
                        padding=(12),
                        margin=(15),
                        width=160,
                        height=130,
                        bgcolor=colors.GREY,
                        border_radius=10,
                        animate_opacity=300,

                        content=Column(spacing=35, controls=[
                            Row(alignment=MainAxisAlignment.END, controls=[
                                tachesvalue,

                            ]),
                            Text(
                                value="Taches",
                                size=20,
                                weight=FontWeight.BOLD,
                                color="WHITE",

                            ),

                        ], ),

                    ),

                ], ),

            ]),

            Column(alignment=alignment.center, controls=[

                Row(alignment=MainAxisAlignment.CENTER, controls=[
                    Container(
                        on_click=button_click,
                        padding=(12),
                        margin=(15),
                        width=160,
                        height=130,
                        bgcolor=colors.GREY,
                        border_radius=10,
                        animate_opacity=300,

                        content=Column(spacing=35, controls=[
                            Row(alignment=MainAxisAlignment.END, controls=[
                                dashboardvalue,

                            ]),
                            Text(
                                value="Dashboard",
                                size=20,
                                weight=FontWeight.BOLD,
                                color="WHITE",

                            ),

                        ], ),

                    ),
                    Container(
                        on_click=ok,
                        padding=(12),
                        margin=(15),
                        width=160,
                        height=130,
                        bgcolor=colors.GREY,
                        border_radius=10,
                        animate_opacity=300,

                        content=Column(spacing=35, controls=[
                            Row(alignment=MainAxisAlignment.END, controls=[
                                entreprisevalue,

                            ]),
                            Text(
                                value="Entreprises",
                                size=20,
                                weight=FontWeight.BOLD,
                                color="WHITE",

                            ),

                        ], ),

                    ),

                ], ),

            ]),

            Column(alignment=alignment.center, controls=[

                Row(alignment=MainAxisAlignment.CENTER, controls=[
                    Container(
                        padding=(12),
                        margin=(15),
                        width=160,
                        height=130,
                        bgcolor=colors.GREY,
                        border_radius=10,
                        animate_opacity=300,

                        content=Column(spacing=35, controls=[
                            Row(alignment=MainAxisAlignment.END, controls=[
                                notesvalue,

                            ]),
                            Text(
                                value="Notes",
                                size=20,
                                weight=FontWeight.BOLD,
                                color="WHITE",

                            ),

                        ], ),

                    ),
                    Container(
                        on_click=ok,
                        padding=(12),
                        margin=(15),
                        width=160,
                        height=130,
                        bgcolor=colors.GREY,
                        border_radius=10,
                        animate_opacity=300,

                        content=Column(spacing=35, controls=[
                            Row(alignment=MainAxisAlignment.END, controls=[
                                affairesvalue,

                            ]),
                            Text(
                                value="Affairs",
                                size=20,
                                weight=FontWeight.BOLD,
                                color="WHITE",

                            ),

                        ], ),

                    ),

                ], ),

            ]),

            Column(alignment=alignment.center, controls=[

                Row(alignment=MainAxisAlignment.CENTER, controls=[
                    Container(


                        padding=(12),
                        margin=(15),
                        width=160,
                        height=130,
                        bgcolor=colors.GREY,
                        border_radius=10,
                        animate_opacity=300,

                        content=Column(spacing=35, controls=[
                            Row(alignment=MainAxisAlignment.END, controls=[
                                piecesvalue,

                            ]),
                            Text(
                                value="Pieces",
                                size=20,
                                weight=FontWeight.BOLD,
                                color="WHITE",

                            ),

                        ], ),

                    ),
                    Container(
                        on_click=ok,
                        padding=(12),
                        margin=(15),
                        width=160,
                        height=130,
                        bgcolor=colors.GREY,
                        border_radius=10,
                        animate_opacity=300,

                        content=Column(spacing=35, controls=[
                            Row(alignment=MainAxisAlignment.END, controls=[
                                produitvalue,

                            ]),
                            Text(
                                value="Produit",
                                size=20,
                                weight=FontWeight.BOLD,
                                color="WHITE",

                            ),

                        ], ),

                    ),

                ], ),

            ]),


       ]
        ),)









        searchbar = Container(alignment=alignment.center,
            padding=(5),

            #margin=(1),
            width=page.window_width,
            height=60,
            bgcolor=colors.BLACK38,
            border_radius=80,
            #animate_opacity=300,
            #alignment=alignment.center,



            content=Container(height=40,width=page.window_width,padding=5, alignment=alignment.center,content=Row([
                TextField(border="NONE",hint_text="Resherche", expand=True),
                IconButton(icon=icons.SEARCH,icon_color=colors.WHITE),

        ],alignment=MainAxisAlignment.SPACE_BETWEEN,)))



        iconss = Container(width=70,content=Column([
            Row(controls=[
                IconButton(icon=icons.EMAIL,icon_color=colors.WHITE70),
                IconButton(icon=icons.CALL,icon_color=colors.WHITE70)
            ]),


        ]))

        listt = ListTile(

                                height=70,
                                autofocus=False,

                                leading=CircleAvatar(width=50,
                                foreground_image_url="https://avatars.githubusercontent.com/u/5041459?s=88&v=4"),
                                title=nameprofile,
                                subtitle=Container(Column(spacing=2,controls=[
                                                logo,
                                                emm,
                                                nuum,

                                            ])),
                                selected=False,

                                trailing=iconss

                            )

        bars = Container(padding=0,content=Column(spacing=5,controls=[


                            Row(alignment='spaceBetween',controls=[
                            Container(

                                content=Row(spacing=2,controls=[
                                    IconButton(icon_size=15, icon=icons.ARROW_BACK_IOS_NEW, on_click=ok),
                                    Text("Contacts", size=15,color=colors.WHITE, weight=FontWeight.BOLD,),

                                ])

                            ),
                            TextButton("MODIFIER",icon_color=colors.WHITE),



                        ],),]))
        import math

        dr = ListView(expand=1, spacing=10, padding=0, auto_scroll=False)
        dr.controls.append(
            Container(

                # gradient=LinearGradient(
                #     begin=alignment.top_left,
                #     end=Alignment(0.8, 1),
                #     colors=[
                #         "0xff1f005c",
                #         "0xff5b0060",
                #         "0xff870160",
                #         "0xffac255e",
                #         "0xffca485c",
                #         "0xffe16b5c",
                #         "0xfff39060",
                #         "0xffffb56b",
                #     ],
                #     tile_mode=GradientTileMode.MIRROR,
                #     rotation=math.pi / 3,
                # ),
                height=150, alignment=alignment.center, content=Column(controls=[
                    bars,
                    listt,

                ], )),



        )

        dr.controls.append(
            Container(padding=5, content=Column(controls=[

                Text("Nom"),
                nomsok,
                Text("Prenom"),
                prenomok,

                Container(content=Column(spacing=10, controls=[

                    Row(alignment=MainAxisAlignment.SPACE_BETWEEN,spacing=20, controls=[
                        Container(
                            content=Row(spacing=5, controls=[
                                Column(controls=[
                                    Text("Email"),
                                    emailsok,
                                ]),

                            ],alignment=MainAxisAlignment.CENTER )

                        ),
                        Column(spacing=10, alignment=alignment.center, controls=[
                            #Text("Optin Mail", size=12),
                            #Switch(width=54, value=True),
                        ]),

                    ], ),

                    Row(spacing=20, controls=[
                        Container(
                            content=Row(alignment="center", spacing=5, controls=[
                                Column(controls=[
                                    Text("Telephone Mobile"),
                                    telephonemobile,
                                ]),

                            ])

                        ),
                        Column(spacing=10, alignment=alignment.center, controls=[
                            Text("Optin SMS", size=12),
                            Switch(width=54, value=True),
                        ]),

                    ],alignment=MainAxisAlignment.SPACE_BETWEEN, ),

                    Row(alignment='spaceBetween', controls=[
                        Container(
                            content=Row(alignment="center", spacing=2, controls=[
                                Column(controls=[
                                    Text("Telephone Fix"),
                                    telephonefix,
                                ]),

                            ])

                        ),

                    ], ),

                    Text("Status"),
                    Row(controls=[
                        ElevatedButton("Prospect", color=colors.BLACK, bgcolor=colors.GREEN_400),
                        ElevatedButton("Client", disabled=True),
                        ElevatedButton("Partnair", disabled=True),
                    ]),

                ]))
                #     Row([
                #
                #         Column(spacing=10, controls=[
                #             Text("Nom"),
                #             TextField(border_color=colors.WHITE70),
                #
                #         ]),
                #         Container(alignment=alignment.center,content=Column(alignment=alignment.center,spacing=5, controls=[
                #             Text("Optin Mail",size=10),
                #             Switch(value=True)
                #
                #         ],)),
                #
                #     ],spacing=20)
                #
                # ],))

            ])),
        )
        if page.route == "/DÉTAIL D’UN CONTACT":
            #page.views.clear()
            page.views.append(
                View(
                    "/DÉTAIL D’UN CONTACTS",
                    [

                        NavigationBar(
                            destinations=[
                                NavigationDestination(icon=icons.INFO, label="Info"),
                                NavigationDestination(icon=icons.EDIT, label="Notes"),
                                NavigationDestination(icon=icons.TASK, label="Taches"),
                                NavigationDestination(icon=icons.CIRCLE_SHARP, label="Affaires"),
                                NavigationDestination(
                                    icon=icons.MENU,
                                    selected_icon=icons.BOOKMARK,
                                    label="Autre",
                                ),
                            ]
                        ),

                            dr,













                ]
                ))














        elif page.route == "/LISTE DES CONTACTS":
            page.views.clear()
            page.views.append(
                View(
                    "/LISTE DES CONTACTS",
                    [

                        AppBar(

                            color="white",
                            toolbar_height=80,
                            leading_width=10,
                            title=searchbar,
                            automatically_imply_leading=False,
                            center_title=True,
                            bgcolor=colors.SURFACE_VARIANT,
                            actions=[
                                IconButton(icons.NOTIFICATIONS_ROUNDED),
                                IconButton(icons.MENU),

                            ],
                        ),

                        Container(height=50,alignment=alignment.center,padding=5,margin=1,

                            content=Row(spacing=0,alignment=MainAxisAlignment.SPACE_BETWEEN,controls=[
                                IconButton(icon_size=15,icon=icons.ARROW_BACK_IOS_NEW,on_click=back),
                                Text("Contacts",size=15,weight=FontWeight.BOLD,width=80),
                                progress,





                            ],)
                                  ),
                        Divider(),

                        ListView(ref=contactlist, expand=1, divider_thickness=1, spacing=10, padding=0, auto_scroll=False),





                    ],
                )
            )

        page.update()


    def godetailscontact(names):
        gp = f'{names}'


        cleaned_data = list(set(contacts))
        cleaned_datas = [(item[0], item[1], item[2]) for item in cleaned_data if item[0] != '']
        normal_list = [list(item) for item in cleaned_datas]

        for c in normal_list:

            if c[0] in gp:
                import json
                print(c[2])
                cs = requests.get(f"https://api-v2.hopcrm.com/api/mobile/contacts/{c[2]}").content
                json_data = json.loads(cs)

                # Extract the desired fields
                contact = json_data['contact']
                nom = contact['nom']
                prenom = contact['prenom']
                nameprofile.value = f'{nom} {prenom}'



                emailx = contact['e_mail']
                telephone_mobile = contact['telephone_mobile']
                telephone_fixe = contact['telephone_fixe']

                telephonefix.value = telephone_fixe
                telephonemobile.value = telephone_mobile
                nomsok.value = nom
                prenomok.value = prenom
                emailsok.value = emailx
                print(emailx)
                if len(emm.value) and len(nuum.value) == 0:
                    emm.value = "None"
                    nuum.value = "None"
                else:
                    emm.value = emailx
                    nuum.value = telephone_mobile



        page.go("/DÉTAIL D’UN CONTACT")

    def ok(e):

        page.go("/LISTE DES CONTACTS")
        llv(contactlist)


    def llv(contactlist):
        import json
        count = 0



        for i in range(13):
            count += 1
            dds = requests.get(f"https://api-v2.hopcrm.com/api/mobile/contacts?page={i}")
            data = json.loads(dds.content)

            for item in data['data']:
                nom = item['nom']
                prenom = item['prenom']
                cle = item['cle']
                contacts.append((nom, prenom, cle))


        contacts.sort(key=lambda x: x[0])

        cleaned_datas = [(item[0], item[1], item[2]) for item in contacts if item[0] != '']
        previous_letter = ''

        for contact in cleaned_datas:
            nom, prenom, cle= contact
            names = Text(f"{nom} {prenom}", color=colors.WHITE)
            if nom:
                first_letter = nom[0].upper()

                # Check if there is a change in the first letter
                if first_letter != previous_letter:
                    contactlist.current.controls.append(ListTile(
                        leading=Text(first_letter, size=30)))

                    # Print the contact information

                    # Update the previous letter
                previous_letter = first_letter

                ss = contactlist.current.controls.append(ListTile(


                    on_click=lambda x, names=names: godetailscontact(names.value),



                    leading=CircleAvatar(
                        foreground_image_url="https://avatars.githubusercontent.com/u/5041459?s=88&v=4"),
                    title=names,

                    subtitle=Text("HOPE OLINE", color=colors.WHITE70),
                    selected=True,

                    trailing=FilledTonalButton(icon_color=colors.GREY,width=105,text="Client",tooltip="Prospect",), ))

        progress.value = 0
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-2]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)



app(target=main)
