node  {
  # Include the ssh module (assuming it's installed)
  include 'ssh'
}

# Disable password authentication
ssh::client::config { 'PasswordAuthentication':
  ensure => 'no',
}

# Set the identity file
ssh::client::config { 'IdentityFile':
  ensure => '~/.ssh/school',
}

