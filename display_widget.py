class DisplayWidget:
    """Class"""
    def __init__(self):
        super().__init__()
        self.stacked_layout = QStackedLaout()
        self.setLayout(self.stacked_layout)
        self.model = None

    def display_results_layout(self):
        self.resuls_table = QTableView()
        
        self.results_layout = QVBoxLayout()
        
        self.resuls_laout.addWidget(self.results_table)
        
        self.results_widget = QWidget
        
        self.results_widget.setLayout(self.results_layout)
        
        self.stacked_layout.addWidget(self.results_widget)
        
