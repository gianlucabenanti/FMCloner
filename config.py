import subprocess,os

filesOLD = [
    "AccountingDocs",
    "AccountingDocsR",
    "AccountingDocsU",
    "Addresses",
    "Articles",
    "ArticlesR",
    "ArticlesU",
    "Badge",
    "Buttons",
    "ButtonsSettings",
    "CallCenter",
    "CallCenterR",
    "CallCenterU",
    "Campaign",
    "CampaignR",
    "CampaignU",
    "Connettore_zS_Contabilita",
    "Connettore_zS_EasyDBC 2",
    "Containers",
    "ContainersR",
    "ContainersU",
    "ControlActivities",
    "ControlActivitiesR",
    "ControlActivitiesU",
    "DataAcquisition",
    "DataRecorded",
    "DataRecordedR",
    "DataRecordedU",
    "Docs",
    "DocsU",
    "EasyDBC_Connector",
    "Events",
    "EventsU",
    "ExternalJobData",
    "ExternalJobDataU",
    "FatturazioneElettronica",
    "GoAppUpdater",
    "GoBadge",
    "GoData",
    "GoInterventions",
    "GoOrders",
    "GoReports",
    "GoSandeza",
    "GoUpdater",
    "Import",
    "ImportS",
    "ImportU",
    "InstallationConfigurator",
    "Installations",
    "InstallationsData",
    "InstallationsR",
    "InstallationsU",
    "InstalledItemsR",
    "InstalledItemsU",
    "Instruments",
    "InstrumentsR",
    "InstrumentsU",
    "Interventions",
    "InterventionsR",
    "InterventionsU",
    "Items",
    "ItemsInstalled",
    "ItemsR",
    "ItemsU",
    "LabelsU",
    "LicenzeFMSandeza",
    "MachineData",
    "MachineImport",
    "MachineImportS",
    "Mec",
    "Menu",
    "Offers",
    "OffersR",
    "OffersU",
    "OperativeDocs",
    "OperativeDocsM",
    "OperativeDocsR",
    "OperativeDocsU",
    "Orders",
    "OrdersR",
    "OrdersRequests",
    "OrdersRequestsU",
    "OrdersU",
    "PackingData",
    "Planning",
    "PlanningU",
    "PreFatEl",
    "ProductionDataU",
    "ProductionUpdate",
    "Projects",
    "ProjectsR",
    "ProjectsU",
    "Protocols",
    "ProtocolsR",
    "ProtocolsU",
    "Provvigioni",
    "ProvvigioniU",
    "Redbooth",
    "Registries",
    "RegistriesR",
    "RegistriesU",
    "Resources",
    "ResourcesR",
    "ResourcesU",
    "SandezaAppleStore",
    "SandezaOffersTool",
    "SandezaSelezioneRU",
    "SandezaWeb",
    "SandezaWebR",
    "SandezaWebW",
    "ServerScripts",
    "stampe_fatel",
    "Stock",
    "StockR",
    "StockU",
    "StockUpdate",
    "Test",
    "Text",
    "Tools",
    "ToolsR",
    "ToolsU",
    "Updater",
    "UserData",
    "zDataManager",
    "zIconeLoghi",
    "zVersioni"
]

command = "fmsadmin list files -u sandezaserver -p s4nd3z4"

# command = "fmsadmin list files -u GianlucaB -p cdzy2we$ch3"

# Funzione per analizzare la stringa di feedback dal terminale
def parse_response(response):
    # definisco i caratteri speciali
    special_characters = ('/', '\\', '\'', '\"')

    # trasformo in stringa
    response = str(response)

    response = response.replace("b'filewin:/", "",)
    response = response.replace("\\r\\nfilewin:/", "\n", )
    response = response.replace("\\r\\n'", "", )

    res = []
    buff = []
    for c in response:
        if c == '\n':
            res.append(''.join(buff))
            buff = []
        else:
            buff.append(c)
    else:
        if buff:
            res.append(''.join(buff))

    return res


def parse_responseOLD(response):
    # definisco i caratteri speciali
    special_characters = ('/', '\\', '\'', '\"')

    # trasformo in stringa
    response = str(response)

    # rimuovo caratteri non supportati da SQL
    for char in special_characters:
        response = response.replace(char, "")

    # rimuovo la 'b' iniziale data da Popen
    if response[0] == 'b':
        response = response[1:]

    return response


# Funzione per eseguire comandi in terminale
def execute_command(command):
    # feedback comando da eseguire
    print('Comando da eseguire ' + str(command))

    # eseguo il comando
    result = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = result.communicate()

    out = parse_response(out)
    err = parse_response(err)

    if ('Error' in out or 'error' in out) and 'evaluation error' not in out:
        err += out
        out = ''

    return out



files = execute_command(command)