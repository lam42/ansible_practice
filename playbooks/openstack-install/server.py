import shade

# Initialize and turn on debug logging
shade.simple_logging(debug=True)

# Initialize cloud
# Cloud configs are read with os-client-config
cloud = shade.openstack_cloud(cloud='mycloud')
