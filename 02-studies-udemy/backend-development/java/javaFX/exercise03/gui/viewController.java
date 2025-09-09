package exercise03.gui;

import javafx.fxml.FXML;
import javafx.scene.control.Button;

public class viewController {
    @FXML
    private button btTest;

    @FXML
    public void onBtTestAction(){
        System.out.println("Click");
    }
}
