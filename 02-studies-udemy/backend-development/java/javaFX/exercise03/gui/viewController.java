package exercise03.gui;

import exercise03.guiUtil.Alerts;
import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;

public class viewController {
    @FXML
    private Button btTest;
    @FXML
    private Button btTest2;

    @FXML
    private void onBtTestAction() {
        Alerts.showAlert("Erro", "Presta Atenção", "Você clicou errado!", Alert.AlertType.INFORMATION);
    }

    @FXML
    private void onBtTestAction2() {
        Alerts.showAlert("Erro", null, "Você clicou errado!", Alert.AlertType.INFORMATION);
    }
}