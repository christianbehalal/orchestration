"""Project settings. There is no need to edit this file unless you want to change values
from the Kedro defaults. For further information, including these default values, see
https://docs.kedro.org/en/stable/kedro_project_setup/settings.html."""

# ✅ Ajout du plugin kedro-mlflow
INSTALLED_PLUGINS = ("kedro_mlflow.framework.hooks.MlflowHook",)

# HOOKS = (ProjectHooks(),)  # Tu peux activer ceci si tu ajoutes tes propres hooks

CONFIG_LOADER_ARGS = {
    "base_env": "base",
    "default_run_env": "local",
    # "config_patterns": {
    #     "spark" : ["spark*/"],
    #     "parameters": ["parameters*", "parameters*/**", "**/parameters*"],
    # }
}
