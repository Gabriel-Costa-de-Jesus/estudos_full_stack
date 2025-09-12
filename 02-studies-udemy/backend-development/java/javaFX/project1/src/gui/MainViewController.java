package gui;

import javafx.fxml.FXML;
import javafx.fxml.Initializable;

import java.awt.*;
import java.net.URL;
import java.util.ResourceBundle;

public class MainViewController implements Initializable {
    @FXML
    private MenuItem menuItemSeller;

    @FXML
    private MenuItem menuItemDepartment;

    @FXML
    private MenuItem menuItemAbout;

    @FXML
    private void onMenuItemSellerAction(){
        System.out.println("O menu intem Seller foi selecionado");
    }

    @FXML
    private void onMenuItemDepartmentAction(){
        System.out.println("O menu intem Departamento foi selecionado");
    }

    @FXML
    private void onMenuItemAboutAction(){
        System.out.println("O menu intem About foi selecionado");
    }

    @Override
    public void initialize(URL uri, ResourceBundle rb) {

    }
}
