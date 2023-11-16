package main

import (
	"bufio"
	"fmt"
	"os"
)

type Dictionary map[string]string

func main() {
	d := make(Dictionary)
	d["example1"] = "definition1"
	d["example2"] = "definition2"
	d["example3"] = "definition3"

	reader := bufio.NewReader(os.Stdin)

	actionAdd(&d, reader)
	actionDefine(&d, reader)
	actionRemove(&d, reader)
	actionList(&d)

}

func actionAdd(d *Dictionary, reader *bufio.Reader) {
	fmt.Print("Entrez la clé du mot que vous voulez ajouter: ")
	key, _ := reader.ReadString('\n')
	fmt.Print("Entrez la valeur: ")
	value, _ := reader.ReadString('\n')

	(*d)[key] = value
	fmt.Println("Le nouveau mot a été ajouté au dictionnaire.")
}

func actionDefine(d *Dictionary, reader *bufio.Reader) {
	fmt.Print("Entrez le mot dont vous voulez accéder à la clé : ")
	key, _ := reader.ReadString('\n')

	if definition, exists := (*d)[key]; exists {
		fmt.Printf("La définition du mot '%s' est : %s\n", key, definition)
	} else {
		fmt.Printf("Le mot '%s' n'existe pas.\n", key)
	}
}

func actionRemove(d *Dictionary, reader *bufio.Reader) {
	fmt.Print("Entrez le mot à supprimer : ")
	word, _ := reader.ReadString('\n')

	if _, exists := (*d)[word]; exists {
		delete(*d, word)
		fmt.Printf("Le mot '%s' a été supprimé.\n", word)
	} else {
		fmt.Printf("Le mot '%s' n'existe pas .\n", word)
	}
}

func actionList(d *Dictionary) {
	fmt.Println("Liste des mots avec leurs définitions:")
	for word, definition := range *d {
		fmt.Printf("Mot: %s, Définition: %s\n", word, definition)
	}
}
