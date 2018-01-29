VERSION 5.00
Begin VB.Form Form1 
   BackColor       =   &H00000000&
   Caption         =   "Form1"
   ClientHeight    =   5475
   ClientLeft      =   120
   ClientTop       =   450
   ClientWidth     =   6660
   LinkTopic       =   "Form1"
   ScaleHeight     =   5475
   ScaleWidth      =   6660
   StartUpPosition =   3  'Windows Default
   Begin VB.CommandButton Command18 
      Caption         =   "/"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   12
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1215
      Left            =   5280
      TabIndex        =   18
      Top             =   4080
      Width           =   975
   End
   Begin VB.CommandButton Command17 
      Caption         =   "*"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   12
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1215
      Left            =   3840
      TabIndex        =   17
      Top             =   4080
      Width           =   975
   End
   Begin VB.CommandButton Command16 
      Caption         =   "_"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   12
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1215
      Left            =   5280
      TabIndex        =   16
      Top             =   2760
      Width           =   975
   End
   Begin VB.CommandButton Command15 
      BackColor       =   &H000000FF&
      Caption         =   "+"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   12
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1215
      Left            =   3840
      TabIndex        =   15
      Top             =   2760
      Width           =   975
   End
   Begin VB.CommandButton Command14 
      Caption         =   "E"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   12
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   615
      Left            =   5280
      TabIndex        =   14
      Top             =   1800
      Width           =   855
   End
   Begin VB.CommandButton Command13 
      Caption         =   "C"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   12
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   615
      Left            =   3840
      TabIndex        =   13
      Top             =   1800
      Width           =   855
   End
   Begin VB.CommandButton Command12 
      Caption         =   "="
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   12
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   735
      Left            =   2520
      TabIndex        =   12
      Top             =   4320
      Width           =   975
   End
   Begin VB.CommandButton Command11 
      Caption         =   "6"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   12
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   735
      Left            =   2520
      TabIndex        =   11
      Top             =   2640
      Width           =   975
   End
   Begin VB.CommandButton Command10 
      Caption         =   "3"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   12
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   735
      Left            =   2520
      TabIndex        =   10
      Top             =   3480
      Width           =   975
   End
   Begin VB.CommandButton Command9 
      Caption         =   "8"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   12
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   735
      Left            =   1440
      TabIndex        =   9
      Top             =   1800
      Width           =   975
   End
   Begin VB.CommandButton Command8 
      Caption         =   "5"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   12
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   735
      Left            =   1440
      TabIndex        =   8
      Top             =   2640
      Width           =   975
   End
   Begin VB.CommandButton Command7 
      Caption         =   "2"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   12
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   735
      Left            =   1440
      TabIndex        =   7
      Top             =   3480
      Width           =   975
   End
   Begin VB.CommandButton Command6 
      Caption         =   "."
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   13.5
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   735
      Left            =   1440
      TabIndex        =   6
      Top             =   4320
      Width           =   975
   End
   Begin VB.CommandButton Command5 
      BackColor       =   &H00C0C0C0&
      Caption         =   "9"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   12
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   735
      Left            =   2520
      MaskColor       =   &H00E0E0E0&
      Style           =   1  'Graphical
      TabIndex        =   5
      Top             =   1800
      Width           =   975
   End
   Begin VB.CommandButton Command4 
      Caption         =   "0"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   12
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   735
      Left            =   360
      TabIndex        =   4
      Top             =   4320
      Width           =   975
   End
   Begin VB.CommandButton Command3 
      Caption         =   "1"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   12
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   735
      Left            =   360
      TabIndex        =   3
      Top             =   3480
      Width           =   975
   End
   Begin VB.CommandButton Command2 
      Caption         =   "4"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   12
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   735
      Left            =   360
      TabIndex        =   2
      Top             =   2640
      Width           =   975
   End
   Begin VB.CommandButton Command1 
      Caption         =   "7"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   12
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   735
      Left            =   360
      TabIndex        =   1
      Top             =   1800
      Width           =   975
   End
   Begin VB.TextBox Text1 
      Alignment       =   1  'Right Justify
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   12
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1095
      Left            =   240
      TabIndex        =   0
      Top             =   240
      Width           =   6135
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Dim op As Double
Dim fn As Double

Private Sub Command1_Click()
Text1.Text = Text1.Text & 7

End Sub

Private Sub Command10_Click()
Text1.Text = Text1.Text & 3
End Sub

Private Sub Command11_Click()
Text1.Text = Text1.Text & 6


End Sub

Private Sub Command12_Click()
If op = 1 Then
Text1.Text = Val(fn) + Val(Text1.Text)
ElseIf op = 2 Then
Text1.Text = Val(fn) - Val(Text1.Text)
ElseIf op = 3 Then
Text1.Text = Val(fn) * Val(Text1.Text)
ElseIf op = 4 Then
Text1.Text = Val(fn) / Val(Text1.Text)
End If


End Sub

Private Sub Command13_Click()
Text1.Text = ""

End Sub

Private Sub Command14_Click()
Unload Me
End Sub

Private Sub Command15_Click()
op = 1
fn = Text1.Text
Text1.Text = ""

End Sub

Private Sub Command16_Click()
op = 2

fn = Text1.Text


Text1.Text = ""
End Sub

Private Sub Command17_Click()
op = 3
fn = Text1.Text

Text1.Text = ""
End Sub

Private Sub Command18_Click()
op = 4
fn = Text1.Text
Text1.Text = ""
End Sub

Private Sub Command2_Click()
Text1.Text = Text1.Text & 4
End Sub

Private Sub Command3_Click()
Text1.Text = Text1.Text & 1
End Sub


Private Sub Command4_Click()
Text1.Text = Text1.Text & 0
End Sub

Private Sub Command5_Click()
Text1.Text = Text1.Text & 9
End Sub

Private Sub Command6_Click()
Text1.Text = Text1.Text & "."
End Sub

Private Sub Command7_Click()
Text1.Text = Text1.Text & 2
End Sub

Private Sub Command8_Click()
Text1.Text = Text1.Text & 5
End Sub

Private Sub Command9_Click()
Text1.Text = Text1.Text & 8
End Sub
