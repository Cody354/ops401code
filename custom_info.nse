-- Custom script to get hostname and processes

local hostname = ""
local processes = {}

function target(host, port)
  -- Get hostname with DNS
  local resolver, err = resolvers.create()
  if err then
    print(err)
    return
  end
  hostname = resolver:gethostbyname(host)
  resolver:destroy()

  -- Simulate process listing (replace with real implementation)
  processes = {"sshd", "apache2", "nginx"}
end

function post_script(host, port)
  print("Target Hostname:", hostname)
  print("Processes:")
  for _, process in ipairs(processes) do
    print("\t", process)
  end
end

local args = {}
args.host = opt.host

script = {
  name = "Custom Host Info",
  author = "Your Name",
  version = "1.0",
  capabilities = {"takes_arguments"},
  arguments = args,
  target = target,
  post_script = post_script
}

return script
