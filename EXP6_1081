{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ATycnspqWJbo",
        "outputId": "b57b92ac-6114-409d-94db-f1f5ee32fafc"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'Effort (Person-Months)': 31.26, 'Time (Months)': 10.7, 'Team Size (Avg Developers)': 2.92}\n"
          ]
        }
      ],
      "source": [
        "def cocomo_basic(kloc, project_type):\n",
        "    cocomo_params = {\n",
        "       \"organic\": (2.6, 1.08, 2.7, 0.40),\n",
        "        \"semi-detached\": (3.2, 1.15, 2.7, 0.37),\n",
        "        \"embedded\": (3.8, 1.25, 2.7, 0.34)\n",
        "\n",
        "    }\n",
        "\n",
        "    if project_type.lower() not in cocomo_params:\n",
        "        return \"Invalid project type! Choose from: organic, semi-detached, embedded.\"\n",
        "\n",
        "\n",
        "    a, b, c, d = cocomo_params[project_type.lower()]\n",
        "\n",
        "\n",
        "    effort = a * (kloc ** b)\n",
        "    time = c * (effort ** d)\n",
        "\n",
        "    avg_team_size = effort / time\n",
        "\n",
        "    return {\n",
        "        \"Effort (Person-Months)\": round(effort, 2),\n",
        "        \"Time (Months)\": round(time, 2),\n",
        "        \"Team Size (Avg Developers)\": round(avg_team_size, 2)\n",
        "    }\n",
        "\n",
        "# Example\n",
        "kloc = 10\n",
        "project_type = \"organic\"\n",
        "\n",
        "result = cocomo_basic(kloc, project_type)\n",
        "print(result)"
      ]
    }
  ]
}
