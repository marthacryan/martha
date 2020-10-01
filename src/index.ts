import {
  JupyterFrontEnd, JupyterFrontEndPlugin
} from '@jupyterlab/application';


/**
 * Initialization data for the martha extension.
 */
const extension: JupyterFrontEndPlugin<void> = {
  id: 'martha',
  autoStart: true,
  activate: (app: JupyterFrontEnd) => {
    console.log('JupyterLab extension martha is activated!');
  }
};

export default extension;
