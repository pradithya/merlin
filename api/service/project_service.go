// Copyright 2020 The Merlin Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package service

import (
	"context"

	"github.com/gojek/merlin/mlp"
)

type ProjectsService interface {
	List(ctx context.Context, projectName string) (mlp.Projects, error)
	GetByID(ctx context.Context, projectID int32) (mlp.Project, error)
	GetByName(ctx context.Context, projectName string) (mlp.Project, error)
}

func NewProjectsService(mlpApiClient mlp.APIClient) ProjectsService {
	return &projectsService{
		mlpApiClient: mlpApiClient,
	}
}

type projectsService struct {
	mlpApiClient mlp.APIClient
}

func (service *projectsService) List(ctx context.Context, projectName string) (mlp.Projects, error) {
	return service.mlpApiClient.ListProjects(ctx, projectName)
}

func (service *projectsService) GetByID(ctx context.Context, projectID int32) (mlp.Project, error) {
	return service.mlpApiClient.GetProjectByID(ctx, projectID)
}

func (service *projectsService) GetByName(ctx context.Context, projectName string) (mlp.Project, error) {
	return service.mlpApiClient.GetProjectByName(ctx, projectName)
}