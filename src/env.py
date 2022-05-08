settings = {
  'wifiAP': 'RSA_Device',
  'wifiPassword': 'WeLoveRSA',
  'controllerName': 'grow-controller', # Used for DHCP hostname
  'logInclude': ['.*'], # regex supported
  'logExclude': [], # regex supported
  'httpTimeout': 2, # seconds

  # Auto-Updating
  'githubRemote': 'https://github.com/rsadelft/RSA_lock',
  'githubUsername': 'SkyloveQiu', # Optional: Without this, you may hit API limits
  'githubToken': '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', # Optional: Without this, you may hit API limits0
  'githubRemoteBranch': "master"
}
