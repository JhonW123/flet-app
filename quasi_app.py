import flet as ft
from flet import Checkbox, Column, FloatingActionButton, Page, Row,Tabs, TextField, UserControl, Text, icons, Container, padding, Divider, colors, alignment, MainAxisAlignment, margin

class Exchange(UserControl):
    # initialization or constructor method of
    def build(self):
        self.fecha = ft.TextField(label="Fecha de la Transaccion",border=ft.InputBorder.UNDERLINE,color=ft.colors.BLACK,width=200)
        self.marketrate = ft.TextField(label="Tasa Mercado (Bs x 1 USD)",border=ft.InputBorder.UNDERLINE,color=ft.colors.BLACK,width=200)
        
       
        
    """def tabs_changed(self, event):
        pass
    
    def update(self):
        status = self.tabs_filter.tabs[self.tabs_filter.selected_index].text
        super().update()"""
         
def main(page: ft.Page):
    
    m = Column(
        width=400,
        alignment="center",
        controls=[
            Row(
                controls=[
                    Row(
                        controls=[
                            ft.Text(
                                "X-Change App",
                                size=50,
                                color=ft.colors.GREEN,
                                bgcolor=ft.colors.WHITE54,
                                weight=ft.FontWeight.BOLD,
                            )
                        ] 
                    )   
                ],
                alignment=ft.MainAxisAlignment.END, 
            ),
        ]
    )
    
    # bloque de inputs de ficha venta
    boton= ft.ElevatedButton("Guardar Compra")
    fecha = ft.TextField(label="Fecha de la Transaccion",border=ft.InputBorder.UNDERLINE,color=ft.colors.BLACK,width=300)
    qtyusd = ft.TextField(label="Cantidad Vendida en USD",border=ft.InputBorder.UNDERLINE,color=ft.colors.BLACK,width=300,autofocus=True)
    marketrate = ft.TextField(label="Tasa Mercado (Bs x 1 USD)",border=ft.InputBorder.UNDERLINE,border_color="white",color=ft.colors.GREEN,hint_text="Enter text here",width=300,autofocus=True, cursor_color="white")
    buyer = ft.TextField(label="Comprador",border=ft.InputBorder.UNDERLINE, color=ft.colors.BLACK,width=300)
    seller = ft.TextField(label="Vendedor",border=ft.InputBorder.UNDERLINE,color=ft.colors.BLACK,width=300)
    qtybs = ft.TextField(label="Cantidad Recibida en Bs.",border=ft.InputBorder.UNDERLINE,color=ft.colors.BLACK,width=300) 
    confirmacion = ft.TextField(label="N° de Confirmacion",border=ft.InputBorder.UNDERLINE,color=ft.colors.BLACK,width=300)
    comments = ft.TextField(label="Ingrese otros detalles de la transaccion",border=ft.InputBorder.UNDERLINE,color=ft.colors.BLACK,width=300)
    buy  = ft.Text("Compra",size=30)
    sale  = ft.Text("Venta",size=30)
    permuta = ft.Text("Swap",size=30)
    
    # bloque de inputs de ficha compra
    botoncom = ft.ElevatedButton("Guardar Compra")
    fechacom = ft.TextField(label="Fecha de la Transaccion",border=ft.InputBorder.UNDERLINE,color=ft.colors.BLACK,width=300)
    qtyusdcom = ft.TextField(label="Cantidad Adquirida en USD",border=ft.InputBorder.UNDERLINE,color=ft.colors.BLACK,width=300,autofocus=True)
    marketratecom = ft.TextField(label="Tasa Mercado (Bs x 1 USD)",border=ft.InputBorder.UNDERLINE,border_color="white",color=ft.colors.GREEN,hint_text="Enter text here",width=300,autofocus=True, cursor_color="white")
    buyercom = ft.TextField(label="Comprador",border=ft.InputBorder.UNDERLINE, color=ft.colors.BLACK,width=300)
    sellercom = ft.TextField(label="Vendedor",border=ft.InputBorder.UNDERLINE,color=ft.colors.BLACK,width=300)
    qtybscom = ft.TextField(label="Monto pagado en Bs.",border=ft.InputBorder.UNDERLINE,color=ft.colors.BLACK,width=300) 
    confirmacioncom = ft.TextField(label="N° de Confirmacion",border=ft.InputBorder.UNDERLINE,color=ft.colors.BLACK,width=300)
    commentscom = ft.TextField(label="Ingrese otros detalles de la transaccion",border=ft.InputBorder.UNDERLINE,color=ft.colors.BLACK,width=300)
    buycom  = ft.Text("Compra",size=30)
    salecom  = ft.Text("Venta",size=30)
    permutacom = ft.Text("Swap",size=30)

    # bloque de inputs de ficha swap
    botonsw = ft.ElevatedButton("Guardar Compra")
    fechasw = ft.TextField(label="Fecha de la Transaccion",border=ft.InputBorder.UNDERLINE,color=ft.colors.BLACK,width=300)
    qtyusdsw = ft.TextField(label="Cantidad Swapeada en USD",border=ft.InputBorder.UNDERLINE,color=ft.colors.BLACK,width=300,autofocus=True)
    marketratesw = ft.TextField(label="Tasa Mercado (Bs x 1 USD)",border=ft.InputBorder.UNDERLINE,border_color="white",color=ft.colors.GREEN,hint_text="Enter text here",width=300,autofocus=True, cursor_color="white")
    buyersw = ft.TextField(label="Comprador",border=ft.InputBorder.UNDERLINE, color=ft.colors.BLACK,width=300)
    sellersw = ft.TextField(label="Cambiador",border=ft.InputBorder.UNDERLINE,color=ft.colors.BLACK,width=300)
    qtybssw = ft.TextField(label="Monto pagado en Bs.",border=ft.InputBorder.UNDERLINE,color=ft.colors.BLACK,width=300) 
    confirmacionsw = ft.TextField(label="N° de Confirmacion",border=ft.InputBorder.UNDERLINE,color=ft.colors.BLACK,width=300)
    commentssw = ft.TextField(label="Ingrese otros detalles de la transaccion",border=ft.InputBorder.UNDERLINE,color=ft.colors.BLACK,width=300)
    buysw  = ft.Text("Compra",size=30)
    salesw  = ft.Text("Venta",size=30)
    permutasw = ft.Text("Swap",size=30)

    ### Prueba de dropdown
    """def dropdown_panama(e):   
        z= ft.Dropdown(
        label="Recepcion de los fondos",
        hint_text="Por favor seleccione una opcion?",
        width=200,
        options=[
            ft.dropdown.Option("Mony Panama"),
            ft.dropdown.Option("Banesco Panama"),
            ft.dropdown.Option("Cash"),
            ],
        )
        page.add(z)
        page.update()
            
    def dropdown_usa(e):
        usa =ft.Dropdown(
            label="Recepcion de los fondos",
            hint_text="Por favor seleccione una opcion?",
            width=200,
            options=[
                ft.dropdown.Option("Bank of America"),
                ft.dropdown.Option("Chase Bank"),
                ft.dropdown.Option("Wells Fargo"),
            ],
        )      
        page.add(usa)
        page.update()
    
    def bancoemisor_func(e):
        if bancoemisor.value == "Banco en Panama": 
            dropdown_panama(e)
        elif bancoemisor.value == "Banco en USA":
            dropdown_usa(e)
        else:
            r = ft.Text("Esto es una prueba")
            page.add(r)
            page.update()"""        
    
         
    bancoemisor = ft.Dropdown(
            label="Forma de entrega de las divisas",
            hint_text="Por favor seleccione una opcion?",
            width=200,
            options=[
            ft.dropdown.Option("Banco en Panama"),
            ft.dropdown.Option("Banco en USA"),
            ft.dropdown.Option("Cash"),
            ],
        )
      
    bancoreceptor = ft.Dropdown(
            label="Salida de los fondos",
            hint_text="Por favor seleccione una opcion?",
            width=200,
            options=[
            ft.dropdown.Option("Banco en Venezuela"),
            ft.dropdown.Option("Banco en Panama"),
            ft.dropdown.Option("Banco en USA"),
            ft.dropdown.Option("Cash"),
        ],
    )
    # z es la variable de la ficha Compra
    
    # u es la variable de la ficha Venta
    u= Container(
        width=100, 
        height=100,
        bgcolor="yellow",
        border_radius=40,
        padding=20,
        margin=(5),
        content=Column(
            controls=[
                Container(
                    width=800, 
                    height=400, 
                    bgcolor="green",
                    border_radius=20,
                    content=Column(
                        spacing=10,
                        controls=[                
                            Column(
                                width=400,
                                controls=[
                                    Row(spacing=10,
                                        run_spacing=10,
                                        controls=[
                                            fecha,
                                            sale,
                                        ],
                                    ),
                                    Column(
                                        controls=[
                                            Row(
                                                controls=[       
                                                    marketrate,
                                                    bancoreceptor, 
                                                ]     
                                            )
                                        ]
                                    ),
                                    Row(
                                        controls=[
                                            Text(
                                                "     ",
                                                size=25,
                                                color="black",
                                                weight="bold",
                                            ),    
                                            qtyusd,
                                            buyer,
                                        ],
                                    ),
                                    Column(
                                        controls=[
                                            Row(
                                                controls=[
                                                    confirmacion,
                                                    ft.ElevatedButton("Guardar Venta")
                                                ]     
                                            )
                                        ]
                                    ),
                                ],
                                expand=1,
                            )
                        ]
                    )
                )
            ]
        )
    )
    # r es la variable de la ficha Swap
    r = Container(
        width=100, 
        height=100,
        bgcolor="yellow",
        border_radius=40,
        padding=20,
        content=Column(
            controls=[
                Container(
                    width=800, 
                    height=460, 
                    bgcolor="yellow",
                    border_radius=20,
                    alignment=alignment.top_left,
                    content=Column(
                        spacing=10,
                        controls=[
                            Row(
                                controls=[
                                    Row(
                                        controls=[
                                            Text(
                                                " ",
                                                size=25,
                                                color="black",
                                                weight="bold",
                                            ),
                                            Text(
                                                "Swap",
                                                size=35,
                                                color="black",
                                                weight="bold",
                                            ),
                                            Text(
                                                "           ",
                                                size=35,
                                                color="black",
                                                weight="bold",
                                            ),
                                        ]
                                    )   
                                ]   
                            ),
                            Column(
                                controls=[
                                    Row(
                                        controls=[
                                            Text(
                                                " ",
                                                size=25,
                                                color="black",
                                                weight="bold",
                                            ),
                                            fechacom,
                                            marketratecom,
                                        ]
                                    )   
                                ]   
                            ),
                            Column(
                                controls=[
                                    Row(
                                        controls=[
                                            Text(
                                                " ",
                                                size=25,
                                                color="black",
                                                weight="bold",
                                            ),
                                            qtyusdcom,
                                            qtybscom,
                                        ]
                                    )   
                                ]   
                            ),
                            Column(
                                controls=[
                                    Row(
                                        controls=[
                                            Text(
                                                " ",
                                                size=25,
                                                color="black",
                                                weight="bold",
                                            ),
                                            sellercom,
                                            confirmacioncom,
                                        ]
                                    )   
                                ]   
                            ),
                            Column(
                                controls=[
                                    Row(
                                        controls=[
                                            Text(
                                                " ",
                                                size=25,
                                                color="black",
                                                weight="bold",
                                            ),
                                            commentscom,
                                            bancoreceptor,
                                        ]
                                    )   
                                ]   
                            ),
                            Column(
                                controls=[
                                    Row(
                                        controls=[
                                            Text(
                                                "                                                                   ",
                                                size=25,
                                                color="black",
                                                weight="bold",
                                            ),
                                            ft.ElevatedButton(
                                                "  Guardar Swap  ",
                                                bgcolor="white",
                                            )
                                        ]
                                    )   
                                ]   
                            ),
                        ]
                    ) 
                )
            ]
        )
    )
    
    z = Container(
        width=100, 
        height=100,
        bgcolor="yellow",
        border_radius=40,
        padding=20,
        content=Column(
            controls=[
                Container(
                    width=800, 
                    height=460, 
                    bgcolor="orange",
                    border_radius=20,
                    alignment=alignment.top_left,
                    content=Column(
                        spacing=10,
                        controls=[
                            Row(
                                controls=[
                                    Row(
                                        controls=[
                                            Text(
                                                " ",
                                                size=25,
                                                color="black",
                                                weight="bold",
                                            ),
                                            Text(
                                                "Compra",
                                                size=35,
                                                color="black",
                                                weight="bold",
                                            ),
                                            Text(
                                                "           ",
                                                size=35,
                                                color="black",
                                                weight="bold",
                                            ),
                                        ]
                                    )   
                                ]   
                            ),
                            Column(
                                controls=[
                                    Row(
                                        controls=[
                                            Text(
                                                " ",
                                                size=25,
                                                color="black",
                                                weight="bold",
                                            ),
                                            fechacom,
                                            marketratecom,
                                        ]
                                    )   
                                ]   
                            ),
                            Column(
                                controls=[
                                    Row(
                                        controls=[
                                            Text(
                                                " ",
                                                size=25,
                                                color="black",
                                                weight="bold",
                                            ),
                                            qtyusdcom,
                                            qtybscom,
                                        ]
                                    )   
                                ]   
                            ),
                            Column(
                                controls=[
                                    Row(
                                        controls=[
                                            Text(
                                                " ",
                                                size=25,
                                                color="black",
                                                weight="bold",
                                            ),
                                            sellercom,
                                            confirmacioncom,
                                        ]
                                    )   
                                ]   
                            ),
                            Column(
                                controls=[
                                    Row(
                                        controls=[
                                            Text(
                                                " ",
                                                size=25,
                                                color="black",
                                                weight="bold",
                                            ),
                                            commentscom,
                                            bancoreceptor,
                                        ]
                                    )   
                                ]   
                            ),
                            Column(
                                controls=[
                                    Row(
                                        controls=[
                                            Text(
                                                "                                                                   ",
                                                size=25,
                                                color="black",
                                                weight="bold",
                                            ),
                                            ft.ElevatedButton(
                                                "  Guardar Compra  ",
                                                bgcolor="white",
                                            )
                                        ]
                                    )   
                                ]   
                            ),
                        ]
                    ) 
                )
            ]
        )
    )
    # Esta es la variable de la ficha Reportes. Tiene un container
    w = Container(
        width=100, 
        height=100,
        bgcolor="yellow",
        border_radius=40,
        padding=20,
        content=Column(
            controls=[
                Container(
                    width=800, 
                    height=460, 
                    bgcolor="green",
                    border_radius=20,
                    alignment=alignment.top_left,
                    content=Column(
                        spacing=10,
                        controls=[
                            Row(
                                controls=[
                                    Row(
                                        controls=[
                                            Text(
                                                " ",
                                                size=25,
                                                color="black",
                                                weight="bold",
                                            ),
                                            Text(
                                                "Venta",
                                                size=35,
                                                color="black",
                                                weight="bold",
                                            ),
                                            Text(
                                                "           ",
                                                size=35,
                                                color="black",
                                                weight="bold",
                                            ),
                                        ]
                                    )   
                                ]   
                            ),
                            Column(
                                controls=[
                                    Row(
                                        controls=[
                                            Text(
                                                " ",
                                                size=25,
                                                color="black",
                                                weight="bold",
                                            ),
                                            fecha,
                                            marketrate,
                                        ]
                                    )   
                                ]   
                            ),
                            Column(
                                controls=[
                                    Row(
                                        controls=[
                                            Text(
                                                " ",
                                                size=25,
                                                color="black",
                                                weight="bold",
                                            ),
                                            qtyusd,
                                            qtybs,
                                        ]
                                    )   
                                ]   
                            ),
                            Column(
                                controls=[
                                    Row(
                                        controls=[
                                            Text(
                                                " ",
                                                size=25,
                                                color="black",
                                                weight="bold",
                                            ),
                                            buyer,
                                            confirmacion,
                                        ]
                                    )   
                                ]   
                            ),
                            Column(
                                controls=[
                                    Row(
                                        controls=[
                                            Text(
                                                " ",
                                                size=25,
                                                color="black",
                                                weight="bold",
                                            ),
                                            comments,
                                            bancoemisor,
                                        ]
                                    )   
                                ]   
                            ),
                            Column(
                                controls=[
                                    Row(
                                        controls=[
                                            Text(
                                                "                                                                   ",
                                                size=25,
                                                color="black",
                                                weight="bold",
                                            ),
                                            ft.ElevatedButton(
                                                "  Guardar Venta  ",
                                                bgcolor="white",
                                            )
                                        ]
                                    )   
                                ]   
                            ),
                        ]
                    ) 
                )
            ]
        )
    )

    s = Container(
        width=100, 
        height=100,
        bgcolor="yellow",
        border_radius=40,
        padding=20,
        content=Column(
            controls=[
                Container(
                    width=800, 
                    height=460, 
                    bgcolor="yellow",
                    border_radius=20,
                    alignment=alignment.top_left,
                    content=Column(
                        spacing=10,
                        controls=[
                            Row(
                                controls=[
                                    Row(
                                        controls=[
                                            Text(
                                                " ",
                                                size=25,
                                                color="black",
                                                weight="bold",
                                            ),
                                            Text(
                                                "Swap",
                                                size=35,
                                                color="black",
                                                weight="bold",
                                            ),
                                            Text(
                                                "           ",
                                                size=35,
                                                color="black",
                                                weight="bold",
                                            ),
                                        ]
                                    )   
                                ]   
                            ),
                            Column(
                                controls=[
                                    Row(
                                        controls=[
                                            Text(
                                                " ",
                                                size=25,
                                                color="black",
                                                weight="bold",
                                            ),
                                            fechasw,
                                            marketratesw,
                                        ]
                                    )   
                                ]   
                            ),
                            Column(
                                controls=[
                                    Row(
                                        controls=[
                                            Text(
                                                " ",
                                                size=25,
                                                color="black",
                                                weight="bold",
                                            ),
                                            qtyusdsw,
                                        ]
                                    )   
                                ]   
                            ),
                            Column(
                                controls=[
                                    Row(
                                        controls=[
                                            Text(
                                                " ",
                                                size=25,
                                                color="black",
                                                weight="bold",
                                            ),
                                            sellersw,
                                        ]
                                    )   
                                ]   
                            ),
                            Column(
                                controls=[
                                    Row(
                                        controls=[
                                            Text(
                                                " ",
                                                size=25,
                                                color="black",
                                                weight="bold",
                                            ),
                                            comments,
                                            bancoemisor,
                                        ]
                                    )   
                                ]   
                            ),
                            Column(
                                controls=[
                                    Row(
                                        controls=[
                                            Text(
                                                "                                                                   ",
                                                size=25,
                                                color="black",
                                                weight="bold",
                                            ),
                                            ft.ElevatedButton(
                                                "  Guardar Swap  ",
                                                bgcolor="white",
                                            )
                                        ]
                                    )   
                                ]   
                            ),
                        ]
                    ) 
                )
            ]
        )
    )
    
    # Bloque de codigo de reportes 
    y = Container(
        width=100, 
        height=100,
        bgcolor="yellow",
        border_radius=40,
        padding=20,
        content=Column(
            controls=[
                Container(
                    width=800, 
                    height=460, 
                    bgcolor="0xFFBDBDBD",
                    border_radius=20,
                    alignment=alignment.top_left,
                    content=Column(
                        spacing=10,
                        controls=[
                            Row(
                                controls=[
                                    Row(
                                        controls=[
                                            Text(
                                                " ",
                                                size=25,
                                                color="black",
                                                weight="bold",
                                            ),
                                            Text(
                                                "Reportes",
                                                size=35,
                                                color="black",
                                                weight="bold",
                                            ),
                                            Text(
                                                "           ",
                                                size=35,
                                                color="black",
                                                weight="bold",
                                            ),
                                        ]
                                    )   
                                ]   
                            ),
                            Column(
                                controls=[
                                    Row(
                                        controls=[
                                            Text(
                                                " ",
                                                size=25,
                                                color="black",
                                                weight="bold",
                                            ),
                                            fechasw,
                                            marketratesw,
                                        ]
                                    )   
                                ]   
                            ),
                            Column(
                                controls=[
                                    Row(
                                        controls=[
                                            Text(
                                                " ",
                                                size=25,
                                                color="black",
                                                weight="bold",
                                            ),
                                            qtyusdsw,
                                        ]
                                    )   
                                ]   
                            ),
                            Column(
                                controls=[
                                    Row(
                                        controls=[
                                            Text(
                                                " ",
                                                size=25,
                                                color="black",
                                                weight="bold",
                                            ),
                                            sellersw,
                                        ]
                                    )   
                                ]   
                            ),
                            Column(
                                controls=[
                                    Row(
                                        controls=[
                                            Text(
                                                " ",
                                                size=25,
                                                color="black",
                                                weight="bold",
                                            ),
                                            comments,
                                            bancoemisor,
                                        ]
                                    )   
                                ]   
                            ),
                            Column(
                                controls=[
                                    Row(
                                        controls=[
                                            Text(
                                                "                                                                   ",
                                                size=25,
                                                color="black",
                                                weight="bold",
                                            )
                                        ]
                                    )   
                                ]   
                            ),
                        ]
                    ) 
                )
            ]
        )
    )
    
    # Control de las Tabs
    t = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Compra",
                icon=ft.icons.CURRENCY_EXCHANGE,
                content=z,
                ),
            ft.Tab(
                text="Venta",
                icon=ft.icons.ACCOUNT_BALANCE,
                content=w,
        ),
            ft.Tab(
                text="Swap",
                icon=ft.icons.SWAP_CALLS,
                content=s,
        ),
            ft.Tab(
                text="Reportes",
                icon=ft.icons.SETTINGS,
                content=y,
        ),

        ]
    )


    page.title = "Exchange App"
    page.horizontal_alignment = "start"
    page.bgcolor="gray"
    page.update()
    page.add(m,t) 


    # create application instance
    #clase = Exchange()

    # add application's root control to the page
   
ft.app(target=main)