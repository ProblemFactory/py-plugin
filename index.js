import { exec } from "child_process";
import fs from "fs";
import path from "path";
import _ from "lodash";
import { config, client } from "./core/client/client.js";

if (config.host === "127.0.0.1") {
  client.Option({ code: 1 }, function(err, response) {
    console.log("python服务器启动中");
    exec(`poetry run python main.py  -grpc-host ${config.host} -grpc-port ${config.port} `, { cwd: global.py_plugin_path }, function(err, stdout, stderr) {
      if (err) console.log(err);
    });
  });
}

let dirs = fs.readdirSync(path.join(global.py_plugin_path, "apps")).filter(x => !x.includes("__") && fs.statSync(path.join(global.py_plugin_path, "apps", x)).isDirectory());
global.py_plugin_dirs = dirs;
global.py_plugin_version = [1, 1, 6];
let apps = [];

for (let file of dirs) {
  try {
    let tmp = await import(`./apps/${file}/js/index.js`);
    if (tmp.rule) {
      for (let key of Object.keys(tmp.rule)) {
        apps.push({
          reg: tmp.rule[key].reg,
          describe: tmp.rule[key].describe,
          priority: tmp.rule[key].priority,
          handler: tmp[key],
        });
      }
    }
  } catch (e) {

  }
}

apps = _.sortBy(apps, app => app.priority);

export const rule = {
  proxy: {
    reg: "noCheck",
    priority: 0,
    describe: "proxy",
  },
};

export async function proxy(e) {
  for (let app of apps) {
    if (new RegExp(app.reg).test(e.msg) || app.reg === "noCheck") {
      try {
        let stop = await app.handler(e);
        if (app.reg !== "noCheck") console.log(`py-plugin:${app.handler.name}`);
        if (app.reg === "noCheck" && stop) console.log(`py-plugin:${app.handler.name}`);
        if (stop === true) {
          return true;
        }
      } catch (e) {
        console.log(`py-plugin:${app.handler.name} error:${e}`);
      }
    }
  }
  return false;
}


export class Proxy {
  name = "py-plugin";
  event = "message";
  priority = 0;
  task = {};
  rule = apps.map(app => {
    return {
      reg: app.reg === "noCheck" ? ".*" : app.reg,
      fnc: app.handler.name,
    };
  });

}

for (let app of apps) {
  Proxy.prototype[app.handler.name] = async (e) => {
    return await app.handler(e) === true;
  };
}

console.log(`python插件${global.py_plugin_version.join(".")}初始化~`);