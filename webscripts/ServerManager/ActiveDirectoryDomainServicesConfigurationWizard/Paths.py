#!/bin/python3
from flask import render_template


def load_page():
    return render_template('ActiveDirectoryDomainServicesConfigurationWizard/Paths.html')