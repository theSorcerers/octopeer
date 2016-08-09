class Api::ChangeTabEventsController < ApplicationController
  include TimeHelper
  before_action :set_change_tab_event, only: :show
  before_action only: :create do
    format_time(:change_tab_event)
  end

  def index
    @change_tab_events = ChangeTabEvent.all

    render json: @change_tab_events
  end

  def show
    render json: @change_tab_event
  end

  def create
    @change_tab_event = ChangeTabEvent.new(change_tab_event_params)

    if @change_tab_event.save
      render json: @change_tab_event, status: :created
    else
      render json: @change_tab_event.errors, status: :unprocessable_entity
    end
  end

  private

  def set_change_tab_event
    @change_tab_event = ChangeTabEvent.find(params[:id])
  end

  def change_tab_event_params
    params.require(:change_tab_event).permit(:id, :session_id, :url, :created_at)
  end
end
